import copy
import json
import inspect
from typing import Optional, List, Callable, AsyncGenerator, Union

from funcdesc.parse import parse_func
from pydantic import BaseModel

from .utils.llm import LLM, get_model
from .utils.misc import desc_to_openai_function


__CTX_VARS_NAME__ = "context_variables"


class AgentResponse(BaseModel):
    messages: List[dict]
    context_variables: dict


class AgentAnswer(BaseModel):
    content: str | BaseModel
    details: AgentResponse


class Agent:
    def __init__(
        self,
        name: str,
        instructions: str,
        model: Optional[Union[LLM, str]] = None,
        functions: Optional[List[Callable]] = None,
    ):
        self.name = name
        self.instructions = instructions
        if model is None:
            model = get_model()
        elif isinstance(model, str):
            model = get_model(model)
        self.model = model
        self.functions = {}
        if functions:
            for func in functions:
                self.functions[func.__name__] = func

    def tool(self, func: Callable):
        """
        Add a tool to the agent.
        """
        self.functions[func.__name__] = func
        return self

    def _convert_functions(self) -> List[dict]:
        """Convert function to the format that the model can understand."""
        functions = []

        for func in self.functions.values():
            func_dict = desc_to_openai_function(
                parse_func(func),
                skip_params=[__CTX_VARS_NAME__],
            )
            functions.append(func_dict)
        return functions

    async def handle_tool_calls(
            self, tool_calls: List, context_variables: dict):
        messages = []
        for call in tool_calls:
            func_name = call["function"]["name"]
            params = json.loads(call["function"]["arguments"])
            func = self.functions[func_name]
            if __CTX_VARS_NAME__ in func.__code__.co_varnames:
                params[__CTX_VARS_NAME__] = context_variables
            if inspect.iscoroutinefunction(func):
                result = await func(**params)
            else:
                result = func(**params)
            context_variables[call["id"]] = result
            messages.append({
                "role": "tool",
                "tool_call_id": call["id"],
                "tool_name": func_name,
                "content": repr(result),
            })
        return messages

    async def get_stream(
        self,
        messages: List,
        max_turns: Union[int, float] = float("inf"),
        context_variables: Optional[dict] = None,
        response_format: Optional[BaseModel] = None,
    ):
        history = copy.deepcopy(messages)
        history.insert(0, {"role": "system", "content": self.instructions})
        init_len = len(history)
        if context_variables is None:
            context_variables = {}

        while len(history) - init_len < max_turns:

            message = {}
            history_clear_parsed = copy.deepcopy(history)
            for msg in history_clear_parsed:
                if "parsed" in msg:
                    del msg["parsed"]
            stream = await self.model.get_stream(
                messages=history_clear_parsed,
                tools=self._convert_functions() or None,
                sender=self.name,
                response_format=response_format,
            )
            async for chunk in stream:
                if chunk.get("delim") == "end":
                    message = chunk["complete"]
                    break
                yield chunk

            if response_format is not None:
                content = message.get("content")
                if content:
                    parsed = response_format.model_validate_json(content)
                    message["parsed"] = parsed

            history.append(message)

            if not message["tool_calls"]:
                break

            tool_messages = await self.handle_tool_calls(
                message["tool_calls"],
                context_variables=context_variables,
            )
            history.extend(tool_messages)

        yield AgentResponse(
            messages=history[init_len:],
            context_variables=context_variables,
        )

    async def run_stream(
            self, stream: AsyncGenerator,
            process_chunk: Optional[Callable] = None) -> AgentResponse:
        async for chunk in stream:
            if isinstance(chunk, dict):
                if process_chunk:
                    process_chunk(chunk)
            else:
                return chunk

    async def run(
            self, msg: List | str | BaseModel | AgentAnswer,
            response_format: Optional[BaseModel] = None,
            context_variables: Optional[dict] = None,
            process_chunk: Optional[Callable] = None,
            ) -> AgentAnswer:
        assert isinstance(msg, (list, str, BaseModel, AgentAnswer)), \
            "Message must be a list, string, BaseModel or AgentAnswer"
        if isinstance(msg, AgentAnswer):
            # For acceping the result of previous run or other agent
            msg = msg.content

        # Convert message to the openai message format
        if isinstance(msg, BaseModel):
            messages = [{"role": "user", "content": msg.model_dump_json()}]
        elif isinstance(msg, str):
            messages = [{"role": "user", "content": msg}]
        elif isinstance(msg, list):
            new_messages = []
            for m in msg:
                if isinstance(m, BaseModel):
                    new_messages.append(
                        {"role": "user", "content": m.model_dump_json()})
                elif isinstance(m, str):
                    new_messages.append({"role": "user", "content": m})
                else:
                    assert isinstance(m, dict), \
                        "Message must be a string, BaseModel or dict"
                    new_messages.append(m)
            messages = new_messages
        stream = self.get_stream(
            messages=messages,
            response_format=response_format,
            context_variables=context_variables,
        )
        details = await self.run_stream(stream, process_chunk)
        final_msg = details.messages[-1]
        if response_format:
            content = final_msg.get("parsed")
        else:
            content = final_msg.get("content")
        return AgentAnswer(content=content, details=details)
