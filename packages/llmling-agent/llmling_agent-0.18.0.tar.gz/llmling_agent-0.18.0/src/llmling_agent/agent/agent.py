"""LLMling integration with PydanticAI for AI-powered resource interaction."""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
import time
from typing import TYPE_CHECKING, Any, Literal, cast, overload
from uuid import UUID, uuid4

from llmling import (
    Config,
    DynamicPrompt,
    LLMCallableTool,
    RuntimeConfig,
    StaticPrompt,
    ToolError,
)
from llmling.prompts.models import FilePrompt
from llmling.utils.importing import import_callable
from psygnal import Signal
from psygnal.containers import EventedDict
from pydantic_ai import Agent as PydanticAgent, RunContext
from pydantic_ai.messages import ModelResponse
from pydantic_ai.models import infer_model
from tokonomics import TokenLimits, get_model_limits
from typing_extensions import TypeVar

from llmling_agent.agent.conversation import ConversationManager
from llmling_agent.agent.providers import AgentProvider, HumanProvider, PydanticAIProvider
from llmling_agent.log import get_logger
from llmling_agent.model_utils import can_format_fields, format_instance_for_llm
from llmling_agent.models import AgentContext, AgentsManifest
from llmling_agent.models.agents import ToolCallInfo
from llmling_agent.models.messages import ChatMessage
from llmling_agent.pydantic_ai_utils import (
    extract_usage,
    format_part,
    get_tool_calls,
    to_result_schema,
)
from llmling_agent.responses.models import (
    ImportedResponseDefinition,
    InlineResponseDefinition,
    ResponseDefinition,
)
from llmling_agent.tools.manager import ToolManager
from llmling_agent.utils.inspection import call_with_context, has_argument_type


if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Sequence

    from llmling.config.models import Resource
    from pydantic_ai.agent import EndStrategy, models
    from pydantic_ai.messages import ModelMessage
    from pydantic_ai.result import StreamedRunResult, Usage

    from llmling_agent.common_types import PromptFunction, StrPath, ToolType
    from llmling_agent.models.context import ConfirmationCallback
    from llmling_agent.models.task import AgentTask
    from llmling_agent.tools.base import ToolInfo


logger = get_logger(__name__)

TResult = TypeVar("TResult", default=str)
TDeps = TypeVar("TDeps", default=Any)
AgentType = Literal["ai", "human"] | AgentProvider
JINJA_PROC = "jinja_template"  # Name of builtin LLMling Jinja2 processor


class Agent[TDeps]:
    """Agent for AI-powered interaction with LLMling resources and tools.

    Generically typed with: LLMLingAgent[Type of Dependencies, Type of Result]

    This agent integrates LLMling's resource system with PydanticAI's agent capabilities.
    It provides:
    - Access to resources through RuntimeConfig
    - Tool registration for resource operations
    - System prompt customization
    - Signals
    - Message history management
    - Database logging
    """

    # this fixes weird mypy issue
    conversation: ConversationManager
    description: str | None

    message_received = Signal(ChatMessage[str])  # Always string
    message_sent = Signal(ChatMessage)
    message_exchanged = Signal(ChatMessage)
    tool_used = Signal(ToolCallInfo)
    model_changed = Signal(object)  # Model | None
    chunk_streamed = Signal(str)
    outbox = Signal(ChatMessage[Any], str)  # self, message, prompt

    def __init__(
        self,
        runtime: RuntimeConfig,
        context: AgentContext[TDeps] | None = None,
        *,
        agent_type: AgentType = "ai",
        session_id: str | UUID | None = None,
        model: models.Model | models.KnownModelName | None = None,
        system_prompt: str | Sequence[str] = (),
        name: str = "llmling-agent",
        description: str | None = None,
        tools: Sequence[ToolType] | None = None,
        retries: int = 1,
        result_retries: int | None = None,
        tool_choice: bool | str | list[str] = True,
        end_strategy: EndStrategy = "early",
        defer_model_check: bool = False,
        enable_logging: bool = True,
        confirmation_callback: ConfirmationCallback | None = None,
        debug: bool = False,
        **kwargs,
    ):
        """Initialize agent with runtime configuration.

        Args:
            runtime: Runtime configuration providing access to resources/tools
            context: Agent context with capabilities and configuration
            agent_type: Agent type to use (ai: PydanticAIProvider, human: HumanProvider)
            session_id: Optional id to recover a conversation
            model: The default model to use (defaults to GPT-4)
            system_prompt: Static system prompts to use for this agent
            name: Name of the agent for logging
            description: Description of the Agent ("what it can do")
            tools: List of tools to register with the agent
            retries: Default number of retries for failed operations
            result_retries: Max retries for result validation (defaults to retries)
            tool_choice: Ability to set a fixed tool or temporarily disable tools usage.
            end_strategy: Strategy for handling tool calls that are requested alongside
                          a final result
            defer_model_check: Whether to defer model evaluation until first run
            kwargs: Additional arguments for PydanticAI agent
            enable_logging: Whether to enable logging for the agent
            confirmation_callback: Callback for confirmation prompts
            debug: Whether to enable debug mode
        """
        self._runtime = runtime
        self._debug = debug
        self._context = context or AgentContext[TDeps].create_default(name)
        self._context.confirmation_callback = confirmation_callback
        self._context.runtime = runtime
        self.message_received.connect(self.message_exchanged.emit)
        self.message_sent.connect(self.message_exchanged.emit)
        self.message_sent.connect(self._forward_message)
        self._result_type = None
        # Initialize tool manager
        all_tools = list(tools or [])
        all_tools.extend(runtime.tools.values())  # Add runtime tools directly
        logger.debug("Runtime tools: %s", list(runtime.tools.keys()))
        self._tool_manager = ToolManager(tools=all_tools, tool_choice=tool_choice)

        # Register capability-based tools
        if self._context and self._context.capabilities:
            self._context.capabilities.register_capability_tools(self)

        config_prompts = context.config.system_prompts if context else []
        all_prompts = list(config_prompts)
        if isinstance(system_prompt, str):
            all_prompts.append(system_prompt)
        else:
            all_prompts.extend(system_prompt)

        # Initialize ConversationManager with all prompts
        self.conversation = ConversationManager(
            self,
            initial_prompts=all_prompts,
            session_id=session_id,
        )

        # Initialize provider based on type
        match agent_type:
            case "ai":
                self._provider: AgentProvider = PydanticAIProvider(
                    model=model,
                    system_prompt=system_prompt,
                    tools=self._tool_manager,
                    conversation=self.conversation,
                    retries=retries,
                    end_strategy=end_strategy,
                    result_retries=result_retries,
                    defer_model_check=defer_model_check,
                    context=self._context,
                    debug=debug,
                )
            case "human":
                self._provider = HumanProvider(
                    conversation=self.conversation,
                    name=name,
                    debug=debug,
                )
            case AgentProvider():
                self._provider = agent_type
            case _:
                msg = f"Invalid agent type: {type}"
                raise ValueError(msg)

        # Initialize agent with all tools
        self._pydantic_agent = PydanticAgent(
            model=model,
            system_prompt=system_prompt,
            deps_type=AgentContext,
            tools=[],  # tools get added for each call explicitely
            retries=retries,
            end_strategy=end_strategy,
            result_retries=result_retries,
            defer_model_check=defer_model_check,
            **kwargs,
        )
        self.name = name
        self.description = description
        msg = "Initialized %s (model=%s)"
        logger.debug(msg, self.name, model)

        from llmling_agent.agent import AgentLogger
        from llmling_agent.events import EventManager

        self._logger = AgentLogger(self, enable_logging=enable_logging)
        self._events = EventManager(self, enable_events=True)

        self._pending_tasks: set[asyncio.Task[Any]] = set()
        self._background_task: asyncio.Task[Any] | None = None
        self._connected_agents: set[Agent[Any]] = set()

    @property
    def name(self) -> str:
        """Get agent name."""
        return self._pydantic_agent.name or "llmling-agent"

    @name.setter
    def name(self, value: str | None):
        self._pydantic_agent.name = value

    def set_result_type(
        self,
        result_type: type[TResult] | str | ResponseDefinition | None,
        *,
        tool_name: str | None = None,
        tool_description: str | None = None,
    ):
        """Set or update the result type for this agent.

        Args:
            result_type: New result type, can be:
                - A Python type for validation
                - Name of a response definition
                - Response definition instance
                - None to reset to unstructured mode
            tool_name: Optional override for tool name
            tool_description: Optional override for tool description
        """
        logger.debug("Setting result type to: %s", result_type)
        self._result_type = result_type
        schema = to_result_schema(
            result_type,
            context=self._context,
            tool_name_override=tool_name,
            tool_description_override=tool_description,
        )
        logger.debug("Created schema: %s", schema)

        # Apply schema and settings
        self._pydantic_agent._result_schema = schema
        self._pydantic_agent._allow_text_result = (
            schema.allow_text_result if schema else True
        )

        # Apply retries if from response definition
        match result_type:
            case InlineResponseDefinition() | ImportedResponseDefinition() as definition:
                if definition.result_retries is not None:
                    self._pydantic_agent._max_result_retries = definition.result_retries

    @classmethod
    @asynccontextmanager
    async def open(
        cls,
        config_path: StrPath | Config | None = None,
        *,
        model: models.Model | models.KnownModelName | None = None,
        session_id: str | UUID | None = None,
        system_prompt: str | Sequence[str] = (),
        name: str = "llmling-agent",
        retries: int = 1,
        result_retries: int | None = None,
        end_strategy: EndStrategy = "early",
        defer_model_check: bool = False,
        **kwargs: Any,
    ) -> AsyncIterator[Agent[TDeps]]:
        """Create an agent with an auto-managed runtime configuration.

        This is a convenience method that combines RuntimeConfig.open with agent creation.

        Args:
            config_path: Path to the runtime configuration file or a Config instance
                         (defaults to Config())
            model: The default model to use (defaults to GPT-4)
            session_id: Optional id to recover a conversation
            system_prompt: Static system prompts to use for this agent
            name: Name of the agent for logging
            retries: Default number of retries for failed operations
            result_retries: Max retries for result validation (defaults to retries)
            end_strategy: Strategy for handling tool calls that are requested alongside
                          a final result
            defer_model_check: Whether to defer model evaluation until first run
            **kwargs: Additional arguments for PydanticAI agent

        Yields:
            Configured Agent instance

        Example:
            ```python
            async with Agent.open("config.yml") as agent:
                result = await agent.run("Hello!")
                print(result.data)
            ```
        """
        if config_path is None:
            config_path = Config()
        async with RuntimeConfig.open(config_path) as runtime:
            agent = cls(
                runtime=runtime,
                model=model,
                session_id=session_id,
                system_prompt=system_prompt,
                name=name,
                retries=retries,
                end_strategy=end_strategy,
                result_retries=result_retries,
                defer_model_check=defer_model_check,
                **kwargs,
            )
            try:
                yield agent
            finally:
                # Any cleanup if needed
                pass

    @classmethod
    @asynccontextmanager
    async def open_agent(
        cls,
        config: StrPath | AgentsManifest,
        agent_name: str,
        *,
        # Model configuration
        model: str | models.Model | models.KnownModelName | None = None,
        session_id: str | UUID | None = None,
        result_type: type[TResult] | None = None,
        model_settings: dict[str, Any] | None = None,
        # Tool configuration
        tools: list[ToolType] | None = None,
        tool_choice: bool | str | list[str] = True,
        end_strategy: EndStrategy = "early",
        # Execution settings
        retries: int = 1,
        result_tool_name: str = "final_result",
        result_tool_description: str | None = None,
        result_retries: int | None = None,
        # Other settings
        system_prompt: str | Sequence[str] | None = None,
        enable_logging: bool = True,
    ) -> AsyncIterator[Agent[TDeps]]:
        """Open and configure a specific agent from configuration.

        Args:
            config: Path to agent configuration file or AgentsManifest instance
            agent_name: Name of the agent to load

            # Basic Configuration
            model: Optional model override
            result_type: Optional type for structured responses
            model_settings: Additional model-specific settings
            session_id: Optional id to recover a conversation

            # Tool Configuration
            tools: Additional tools to register (import paths or callables)
            tool_choice: Control tool usage:
                - True: Allow all tools
                - False: No tools
                - str: Use specific tool
                - list[str]: Allow specific tools
            end_strategy: Strategy for handling tool calls that are requested alongside
                            a final result

            # Execution Settings
            retries: Default number of retries for failed operations
            result_tool_name: Name of the tool used for final result
            result_tool_description: Description of the final result tool
            result_retries: Max retries for result validation (defaults to retries)

            # Other Settings
            system_prompt: Additional system prompts
            enable_logging: Whether to enable logging for the agent

        Yields:
            Configured Agent instance

        Raises:
            ValueError: If agent not found or configuration invalid
            RuntimeError: If agent initialization fails

        Example:
            ```python
            async with Agent.open_agent(
                "agents.yml",
                "my_agent",
                model="gpt-4",
                tools=[my_custom_tool],
            ) as agent:
                result = await agent.run("Do something")
            ```
        """
        if isinstance(config, AgentsManifest):
            agent_def = config
        else:
            agent_def = AgentsManifest.from_file(config)

        if agent_name not in agent_def.agents:
            msg = f"Agent {agent_name!r} not found in {config}"
            raise ValueError(msg)

        agent_config = agent_def.agents[agent_name]

        # Use model from override or agent config
        actual_model = model or agent_config.model
        if not actual_model:
            msg = "Model must be specified either in config or as override"
            raise ValueError(msg)
        # Create context
        context = AgentContext[TDeps](
            agent_name=agent_name,
            capabilities=agent_config.capabilities,
            definition=agent_def,
            config=agent_config,
            model_settings=model_settings or {},
        )

        # Set up runtime
        cfg = agent_config.get_config()
        async with RuntimeConfig.open(cfg) as runtime:
            agent = cls(
                runtime=runtime,
                context=context,
                result_type=result_type,
                model=actual_model,  # type: ignore[arg-type]
                retries=retries,
                session_id=session_id,
                result_tool_name=result_tool_name,
                result_tool_description=result_tool_description,
                result_retries=result_retries,
                end_strategy=end_strategy,
                tool_choice=tool_choice,
                tools=tools,
                system_prompt=system_prompt or [],
                enable_logging=enable_logging,
            )
            try:
                yield agent
            finally:
                # Any cleanup if needed
                pass

    def _forward_message(self, message: ChatMessage[Any]):
        """Forward sent messages."""
        logger.debug(
            "forwarding message from %s: %s (type: %s) to %d connected agents",
            self.name,
            repr(message.content),
            type(message.content),
            len(self._connected_agents),
        )
        # update = {"forwarded_from": [*message.forwarded_from, self.name]}
        # forwarded_msg = message.model_copy(update=update)
        message.forwarded_from.append(self.name)
        self.outbox.emit(message, None)

    async def disconnect_all(self):
        """Disconnect from all agents."""
        if self._connected_agents:
            for target in list(self._connected_agents):
                self.stop_passing_results_to(target)

    def pass_results_to(self, other: Agent[Any], prompt: str | None = None):
        """Forward results to another agent."""
        self.outbox.connect(other._handle_message)
        self._connected_agents.add(other)

    def stop_passing_results_to(self, other: Agent[Any]):
        """Stop forwarding results to another agent."""
        if other in self._connected_agents:
            self.outbox.disconnect(other._handle_message)
            self._connected_agents.remove(other)

    def is_busy(self) -> bool:
        """Check if agent is currently processing tasks."""
        return bool(self._pending_tasks or self._background_task)

    @property
    def model_name(self) -> str | None:
        """Get the model name in a consistent format."""
        match self._pydantic_agent.model:
            case str() | None:
                return self._pydantic_agent.model
            case _:
                return self._pydantic_agent.model.name()

    def _update_tools(self):
        """Update pydantic-ai-agent tools."""
        agent = self._pydantic_agent
        agent._function_tools.clear()
        tools = [t for t in self.tools.values() if t.enabled]
        for tool in tools:
            wrapped = (
                self._context.wrap_tool(tool, self._context)
                if self._context
                else tool.callable.callable
            )
            if has_argument_type(wrapped, "RunContext"):
                agent.tool(wrapped)
            else:
                agent.tool_plain(wrapped)

    async def run(
        self,
        *prompt: str,
        result_type: type[TResult] | None = None,
        deps: TDeps | None = None,
        message_history: list[ModelMessage] | None = None,
        model: models.Model | models.KnownModelName | None = None,
        usage: Usage | None = None,
    ) -> ChatMessage[TResult]:
        """Run agent with prompt and get response.

        Args:
            prompt: User query or instruction
            result_type: Optional type for structured responses
            deps: Optional dependencies for the agent
            message_history: Optional previous messages for context
            model: Optional model override
            usage: Optional usage to start with,
                    useful for resuming a conversation or agents used in tools

        Returns:
            Result containing response and run information

        Raises:
            UnexpectedModelBehavior: If the model fails or behaves unexpectedly
        """
        logger.debug("Agent.run result_type = %s", result_type)
        final_prompt = "\n\n".join(
            format_instance_for_llm(p)
            if not isinstance(p, str) and can_format_fields(p)
            else str(p)
            for p in prompt
        )
        wait_for_chain = False  # TODO
        if deps is not None:
            self._context.data = deps
        self.set_result_type(result_type)

        try:
            # Clear all tools
            if self._context:
                self._context.current_prompt = final_prompt
            if model:
                # perhaps also check for old model == new model?
                if isinstance(model, str):
                    model = infer_model(model)
                self.model_changed.emit(model)
            # Register currently enabled tools
            self._update_tools()

            logger.debug("agent run prompt=%s", final_prompt)
            message_id = str(uuid4())

            # Run through pydantic-ai's public interface
            start_time = time.perf_counter()
            msg_history = (
                message_history if message_history else self.conversation.get_history()
            )
            if self._debug:
                from devtools import debug

                debug(self._pydantic_agent)
            result = await self._pydantic_agent.run(
                final_prompt,
                deps=self._context,
                message_history=msg_history,
                model=model,
                usage=usage,
            )
            logger.debug("Agent run result: %r", result.data)
            messages = result.new_messages()
            for call in get_tool_calls(messages, dict(self.tools._items)):
                call.message_id = message_id
                call.context_data = self._context.data if self._context else None
                self.tool_used.emit(call)
            self.conversation._last_messages = list(messages)
            if not message_history:
                self.conversation.set_history(result.all_messages())

            # Emit user message
            _user_msg = ChatMessage[str](content=final_prompt, role="user")
            self.message_received.emit(_user_msg)

            # Get cost info for assistant response
            usage = result.usage()
            cost_info = (
                await extract_usage(
                    usage, self.model_name, final_prompt, str(result.data)
                )
                if self.model_name
                else None
            )

            # Create and emit assistant message
            assistant_msg = ChatMessage[TResult](
                content=result.data,
                role="assistant",
                name=self.name,
                model=self.model_name,
                message_id=message_id,
                cost_info=cost_info,
                response_time=time.perf_counter() - start_time,
            )
            self.message_sent.emit(assistant_msg)

        except Exception:
            logger.exception("Agent run failed")
            raise
        else:
            if wait_for_chain:
                await self.wait_for_chain()
            return assistant_msg
        finally:
            if model:
                # Restore original model in signal
                old = self._pydantic_agent.model
                model_obj = infer_model(old) if isinstance(old, str) else old
                self.model_changed.emit(model_obj)

    @overload
    async def talk_to(
        self,
        agent: str | Agent[TDeps],
        prompt: str,
        *,
        get_answer: Literal[True],
    ) -> ChatMessage[Any]: ...

    @overload
    async def talk_to(
        self,
        agent: str | Agent[TDeps],
        prompt: str,
        *,
        get_answer: Literal[False] = False,
    ) -> None: ...

    async def talk_to(
        self,
        agent: str | Agent[TDeps],
        prompt: str,
        *,
        get_answer: bool = False,
        include_history: bool = False,
        max_tokens: int | None = None,
    ) -> ChatMessage[Any] | None:
        """Send a message to another agent.

        Args:
            agent: Name of agent or agent instance to talk to
            prompt: Message to send
            get_answer: Whether to request a response
            include_history: Whether to send conversation history
            max_tokens: Optional token limit for history

        Example:
            # Share context and get response
            response = await agent1.talk_to(
                "agent2",
                "What do you think about our discussion?",
                get_answer=True,
                include_history=True,
                max_tokens=1000
            )
        """
        assert self._context.pool
        target = (
            agent if isinstance(agent, Agent) else self._context.pool.get_agent(agent)
        )

        if include_history:
            # Add formatted history as context first
            history = await self.conversation.format_history(max_tokens=max_tokens)
            await target.conversation.add_context_message(
                history, source=self.name, metadata={"type": "conversation_history"}
            )

        # Add the new message
        await target.conversation.add_context_message(prompt, source=self.name)

        if get_answer:
            return await target.run(prompt)

        return None

    def to_agent_tool(
        self,
        *,
        name: str | None = None,
        reset_history_on_run: bool = True,
        pass_message_history: bool = False,
        share_context: bool = False,
        parent: Agent[Any] | None = None,
    ) -> LLMCallableTool:
        """Create a tool from this agent.

        Args:
            name: Optional tool name override
            reset_history_on_run: Clear agent's history before each run
            pass_message_history: Pass parent's message history to agent
            share_context: Whether to pass parent's context/deps
            parent: Optional parent agent for history/context sharing
        """
        tool_name = f"ask_{self.name}"

        async def wrapped_tool(ctx: RunContext[AgentContext[TDeps]], prompt: str) -> str:
            if pass_message_history and not parent:
                msg = "Parent agent required for message history sharing"
                raise ToolError(msg)

            if reset_history_on_run:
                self.conversation.clear()

            history = (
                parent.conversation.get_history()
                if pass_message_history and parent
                else None
            )
            deps = ctx.deps.data if share_context else None

            result = await self.run(
                prompt, message_history=history, deps=deps, result_type=self._result_type
            )
            return result.data

        normalized_name = self.name.replace("_", " ").title()
        docstring = f"Get expert answer from specialized agent: {normalized_name}"
        if self.description:
            docstring = f"{docstring}\n\n{self.description}"

        wrapped_tool.__doc__ = docstring
        wrapped_tool.__name__ = tool_name

        return LLMCallableTool.from_callable(
            wrapped_tool,
            name_override=tool_name,
            description_override=docstring,
        )

    @asynccontextmanager
    async def run_stream(
        self,
        *prompt: str,
        result_type: type[TResult] | None = None,
        deps: TDeps | None = None,
        message_history: list[ModelMessage] | None = None,
        model: models.Model | models.KnownModelName | None = None,
        usage: Usage | None = None,
    ) -> AsyncIterator[StreamedRunResult[AgentContext[TDeps], TResult]]:
        """Run agent with prompt and get a streaming response.

        Args:
            prompt: User query or instruction
            result_type: Optional type for structured responses
            deps: Optional dependencies for the agent
            message_history: Optional previous messages for context
            model: Optional model override
            usage:  Optional usage to start with,
                    useful for resuming a conversation or agents used in tools

        Returns:
            A streaming result to iterate over.

        Raises:
            UnexpectedModelBehavior: If the model fails or behaves unexpectedly
        """
        final_prompt = "\n\n".join(
            format_instance_for_llm(p)
            if not isinstance(p, str) and can_format_fields(p)
            else str(p)
            for p in prompt
        )
        self.set_result_type(result_type)

        if deps is not None:
            self._context.data = deps
        try:
            self._update_tools()

            # Emit user message
            _user_msg = ChatMessage[str](content=final_prompt, role="user")
            self.message_received.emit(_user_msg)
            start_time = time.perf_counter()
            msg_history = message_history or self.conversation.get_history()
            async with self._pydantic_agent.run_stream(
                final_prompt,
                message_history=msg_history,
                model=model,
                deps=self._context,
                usage=usage,
            ) as stream:
                original_stream = stream.stream

                async def wrapped_stream(*args, **kwargs):
                    async for chunk in original_stream(*args, **kwargs):
                        self.chunk_streamed.emit(str(chunk))
                        yield chunk

                    if stream.is_complete:
                        message_id = str(uuid4())
                        if not message_history:
                            self.conversation.set_history(stream.all_messages())
                        # TODO: need to properly deal with structured
                        if stream.is_structured:
                            message = stream._stream_response.get(final=True)
                            if not isinstance(message, ModelResponse):
                                msg = "Expected ModelResponse for structured output"
                                raise TypeError(msg)  # noqa: TRY301
                        # Handle captured tool calls
                        messages = stream.new_messages()
                        self.conversation._last_messages = list(messages)
                        for call in get_tool_calls(messages, dict(self.tools._items)):
                            call.message_id = message_id
                            call.context_data = (
                                self._context.data if self._context else None
                            )
                            self.tool_used.emit(call)
                        # Get all model responses and format their parts
                        responses = [m for m in messages if isinstance(m, ModelResponse)]
                        parts = [p for msg in responses for p in msg.parts]
                        content = "\n".join(format_part(p) for p in parts)
                        usage = stream.usage()
                        cost = (
                            await extract_usage(
                                usage, self.model_name, final_prompt, content
                            )
                            if self.model_name
                            else None
                        )

                        # Create and emit assistant message
                        assistant_msg = ChatMessage[TResult](
                            content=cast(TResult, content),
                            role="assistant",
                            name=self.name,
                            model=self.model_name,
                            message_id=message_id,
                            cost_info=cost,
                            response_time=time.perf_counter() - start_time,
                        )
                        self.message_sent.emit(assistant_msg)

                stream.stream = wrapped_stream  # type: ignore
                yield stream

        except Exception:
            logger.exception("Agent stream failed")
            raise

    def run_sync(
        self,
        prompt: str,
        *,
        deps: TDeps | None = None,
        message_history: list[ModelMessage] | None = None,
        model: models.Model | models.KnownModelName | None = None,
    ) -> ChatMessage[TResult]:
        """Run agent synchronously (convenience wrapper).

        Args:
            prompt: User query or instruction
            deps: Optional dependencies for the agent
            message_history: Optional previous messages for context
            model: Optional model override

        Returns:
            Result containing response and run information
        """
        try:
            return asyncio.run(
                self.run(prompt, message_history=message_history, deps=deps, model=model)
            )
        except KeyboardInterrupt:
            raise
        except Exception:
            logger.exception("Sync agent run failed")
            raise

    async def complete_tasks(self):
        """Wait for all pending tasks to complete."""
        if self._pending_tasks:
            await asyncio.wait(self._pending_tasks)

    async def wait_for_chain(self, _seen: set[str] | None = None):
        """Wait for this agent and all connected agents to complete their tasks."""
        # Track seen agents to avoid cycles
        seen = _seen or {self.name}

        # Wait for our own tasks
        await self.complete_tasks()

        # Wait for connected agents
        for agent in self._connected_agents:
            if agent.name not in seen:
                seen.add(agent.name)
                await agent.wait_for_chain(seen)

    async def run_task[TResult](
        self,
        task: AgentTask[TDeps, TResult],
        *,
        result_type: type[TResult] | None = None,
    ) -> ChatMessage[TResult]:
        """Execute a pre-defined task.

        Args:
            task: Task configuration to execute
            result_type: Optional override for task result type

        Returns:
            Task execution result

        Raises:
            TaskError: If task execution fails
            ValueError: If task configuration is invalid
        """
        from llmling_agent.tasks import TaskError

        if result_type is not None:
            self._pydantic_agent._result_schema = to_result_schema(result_type)
        # Load task knowledge
        if task.knowledge:
            # Add knowledge sources to context
            resources: list[Resource | str] = list(task.knowledge.paths) + list(
                task.knowledge.resources
            )
            for source in resources:
                await self.conversation.load_context_source(source)
            for prompt in task.knowledge.prompts:
                if isinstance(prompt, StaticPrompt | DynamicPrompt | FilePrompt):
                    await self.conversation.add_context_from_prompt(prompt)
                else:
                    await self.conversation.load_context_source(prompt)

        # Register task tools
        original_tools = dict(self.tools._items)  # Store original tools
        try:
            for tool_config in task.tool_configs:
                callable_obj = import_callable(tool_config.import_path)
                # Create LLMCallableTool with optional overrides
                llm_tool = LLMCallableTool.from_callable(
                    callable_obj,
                    name_override=tool_config.name,
                    description_override=tool_config.description,
                )

                # Register with ToolManager
                meta = {"import_path": tool_config.import_path}
                self.tools.register_tool(llm_tool, source="task", metadata=meta)
            # Execute task with default strategy
            from llmling_agent.tasks.strategies import DirectStrategy

            strategy = DirectStrategy[TDeps, TResult]()
            agent = cast(Agent[TDeps], self)
            return await strategy.execute(task=task, agent=agent)

        except Exception as e:
            msg = f"Task execution failed: {e}"
            logger.exception(msg)
            raise TaskError(msg) from e

        finally:
            # Restore original tools
            self.tools._items = EventedDict(original_tools)

    async def run_continuous(
        self,
        prompt: str | PromptFunction,
        *,
        max_count: int | None = None,
        interval: float = 1.0,
        block: bool = False,
        **kwargs: Any,
    ) -> ChatMessage[TResult] | None:
        """Run agent continuously with prompt or dynamic prompt function.

        Args:
            prompt: Static prompt or function that generates prompts
            max_count: Maximum number of runs (None = infinite)
            interval: Seconds between runs
            block: Whether to block until completion
            **kwargs: Arguments passed to run()
        """

        async def _continuous():
            count = 0
            while max_count is None or count < max_count:
                try:
                    current_prompt = (
                        prompt
                        if isinstance(prompt, str)
                        else call_with_context(prompt, self._context, **kwargs)
                    )
                    await self.run(current_prompt, **kwargs)
                    await self.run(current_prompt, **kwargs)
                    count += 1
                    await asyncio.sleep(interval)
                except asyncio.CancelledError:
                    break
                except Exception:
                    logger.exception("Background run failed")
                    await asyncio.sleep(interval)

        # Cancel any existing background task
        await self.stop()
        task = asyncio.create_task(_continuous(), name=f"background_{self.name}")

        if block:
            try:
                await task  # Wait for completion if max_count set
                return None
            finally:
                if not task.done():
                    task.cancel()
        else:
            self._background_task = task
            return None

    async def stop(self):
        """Stop continuous execution if running."""
        if self._background_task and not self._background_task.done():
            self._background_task.cancel()
            await self._background_task
            self._background_task = None

    def clear_history(self):
        """Clear both internal and pydantic-ai history."""
        self._logger.clear_state()
        self.conversation.clear()
        for tool in self._pydantic_agent._function_tools.values():
            tool.current_retry = 0
        logger.debug("Cleared history and reset tool state")

    def _handle_message(self, message: ChatMessage[Any], prompt: str | None = None):
        """Handle a message and optional prompt forwarded from another agent."""
        if not message.forwarded_from:
            msg = "Message received in _handle_message without sender information"
            raise RuntimeError(msg)

        sender = message.forwarded_from[-1]
        msg = "_handle_message called on %s from %s with message %s"
        logger.debug(msg, self.name, sender, message.content)

        loop = asyncio.get_event_loop()
        prompts = [str(message.content)]
        if prompt:
            prompts.append(prompt)
        task = loop.create_task(self.run(*prompts))
        self._pending_tasks.add(task)
        task.add_done_callback(self._pending_tasks.discard)
        # for target in self._context.config.forward_to:
        #     match target:
        #         case AgentTarget():
        #             # Create task for agent forwarding
        #             loop = asyncio.get_event_loop()
        #             task = loop.create_task(self.run(str(message.content), deps=source))
        #             self._pending_tasks.add(task)
        #             task.add_done_callback(self._pending_tasks.discard)

        #         case FileTarget():
        #             path = target.resolve_path({"agent": self.name})
        #             path.parent.mkdir(parents=True, exist_ok=True)
        #             path.write_text(str(message.content))

    async def get_token_limits(self) -> TokenLimits | None:
        """Get token limits for the current model."""
        if not self.model_name:
            return None

        try:
            return await get_model_limits(self.model_name)
        except ValueError:
            logger.debug("Could not get token limits for model: %s", self.model_name)
            return None

    def register_worker(
        self,
        worker: Agent[Any],
        *,
        name: str | None = None,
        reset_history_on_run: bool = True,
        pass_message_history: bool = False,
        share_context: bool = False,
    ) -> ToolInfo:
        """Register another agent as a worker tool."""
        return self.tools.register_worker(
            worker,
            name=name,
            reset_history_on_run=reset_history_on_run,
            pass_message_history=pass_message_history,
            share_context=share_context,
            parent=self if (pass_message_history or share_context) else None,
        )

    def set_model(self, model: models.Model | models.KnownModelName | None):
        """Set the model for this agent.

        Args:
            model: New model to use (name or instance)

        Emits:
            model_changed signal with the new model
        """
        old_name = self.model_name
        if isinstance(model, str):
            model = infer_model(model)
        self._pydantic_agent.model = model
        self.model_changed.emit(model)
        logger.debug("Changed model from %s to %s", old_name, self.model_name)

    def result_validator(self, *args: Any, **kwargs: Any) -> Any:
        """Register a result validator.

        Validators can access runtime through RunContext[AgentContext].

        Example:
            ```python
            @agent.result_validator
            async def validate(ctx: RunContext[AgentContext], result: str) -> str:
                if len(result) < 10:
                    raise ModelRetry("Response too short")
                return result
            ```
        """
        return self._pydantic_agent.result_validator(*args, **kwargs)

    @property
    def runtime(self) -> RuntimeConfig:
        """Get the runtime configuration."""
        return self._runtime

    @property
    def tools(self) -> ToolManager:
        return self._tool_manager


if __name__ == "__main__":
    import logging

    from llmling_agent import config_resources

    logging.basicConfig(level=logging.INFO)

    sys_prompt = "Open browser with google, please"

    async def main():
        async with RuntimeConfig.open(config_resources.OPEN_BROWSER) as r:
            agent = Agent[Any](r, model="openai:gpt-4o-mini")
            result = await agent.run(sys_prompt)
            print(result.data)

    asyncio.run(main())
