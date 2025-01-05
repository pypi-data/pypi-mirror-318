import docstring_parser
import inspect

from abc import ABC, abstractmethod
from importlib import import_module
from pydantic import BaseModel, computed_field, ConfigDict, Field, HttpUrl
from typing import Any, Callable, Dict, List, Optional
from typing_extensions import Self

class Message(BaseModel):
  model_config = ConfigDict(extra="allow")
  
  role: str = Field(
    ...,
    description="The role of the message sender."
  )
  name: Optional[str] = Field(
    None,
    description="The name of the message sender."
  )
  content: Optional[str] = Field(
    None,
    description="The text content of the message."
  )
  image: Optional[HttpUrl] = Field(
    None,
    description="The image content of the message."
  )
  audio: Optional[HttpUrl] = Field(
    None,
    description="The audio content of the message."
  )
  files: Optional[List[HttpUrl]] = Field(
    None,
    description="The files attached to the message."
  )
  
class Usage(BaseModel):
  prompt_tokens: int = Field(
    ...,
    description="The number of tokens in the prompt."
  )
  completion_tokens: int = Field(
    ...,
    description="The number of tokens to generate."
  )
  model: str = Field(
    ...,
    description="The model to use for generation."
  )
  
  @computed_field
  @property
  def total_tokens(self) -> int:
    return self.prompt_tokens + self.completion_tokens
  
class FunctionCall(BaseModel):
  name: str = Field(
    ...,
    description="The name of the function to call."
  )
  arguments: str = Field(
    ...,
    description="JSON string of the arguments to pass to the function."
  )
  
class ToolCall(BaseModel):
  id: str = Field(
    ...,
    description="The id of the tool to call."
  )
  function: FunctionCall = Field(
    ...,
    description="The function to call on the tool."
  )
  type: str = Field(
    ...,
    description="The type of the tool to call."
  )
  
class ChatResponse(BaseModel):
  role: str = Field(
    ...,
    description="The role of the message sender."
  )
  content: Optional[str] = Field(
    None,
    description="The text content of the message."
  )
  usage: Usage = Field(
    ...,
    description="The usage of the model."
  )
  tool_calls: Optional[List[ToolCall]] = Field(
    None,
    description="The tools to call."
  )
  
class ChatClient(ABC):
  @abstractmethod
  def complete_chat(
    self,
    messages: List[Message],
    model: str,
    stream: bool = False,
    temperature: float = 0.0,
    tools: Optional[List[Dict[str, Any]]] = None,
    tool_choice: Optional[str|Dict[str, Any]] = None,
    **kwargs
  ) -> ChatResponse:
    pass
  
  @classmethod
  @abstractmethod
  def tool_result_to_message(
    cls,
    tool_call: ToolCall,
    tool_result: str,
    **kwargs
  ) -> Message:
    pass
  
  @classmethod
  def func2json(cls, func: Callable) -> dict:
    """
    Convert a function to a JSON serializable dictionary.
    
    This implementation is tailored for OpenAI's chat API,
    which requires function descriptions to follow a specific
    JSON schema. For other LLM Chat APIs, this method should
    be overridden.
    
    Args:
      func (Callable): The function to convert.
      
    Returns:
      dict: The JSON serializable dictionary.
    """
    type_map = {
      str: "string",
      int: "integer",
      float: "number",
      bool: "boolean",
      list: "array",
      dict: "object",
      type(None): "null"
    }
    
    try:
      signature = inspect.signature(func)
    except ValueError as e:
      raise ValueError(f"Function {func.__name__} has invalid signature: {e}")
    
    doc = docstring_parser.parse(func.__doc__)
    
    arguments = {}
    for param in signature.parameters.values():
      try:
        arg_type = type_map.get(param.annotation, "string")
      except KeyError as e:
        raise KeyError(f"Function {func.__name__} has invalid annotation '{param.annotation}' for parameter '{param.name}': {e}")
      
      description = ""
      for section in doc.params:
        if section.arg_name == param.name:
          description = section.description.strip() if section.description else ""
          break
      
      arguments[param.name] = {
        "type": arg_type,
        "description": description,
      }   
      
    required = [param.name for param in signature.parameters.values() if param.default == inspect._empty]
    
    return {
      "type": "function",
      "function": {
        "name": func.__name__,
        "description": doc.description.strip() if doc.description else "",
        "parameters": {
          "type": "object",
          "properties": arguments,
          "required": required,
        },
      },
    }
    
  @classmethod
  def use(cls, name: str) -> Self:
    # Dynamically import the module containing the chat client
    module_name = name.lower()
    module = import_module(f".{module_name}", __package__)
    # Retrieve the class from the module and ensure it is a subclass of ChatClient
    for obj in module.__dict__.values():
      if isinstance(obj, type) and issubclass(obj, cls) and obj is not cls:
        return obj()
    raise ImportError(f"Module {module_name} does not contain a subclass of ChatClient.")