import json
import tempfile

from openai import OpenAI
from openai.types.beta import Assistant, Thread
from openai.types.chat import ChatCompletion
from pydantic import HttpUrl
from typing import Any, Dict, List, Optional
from mediqbox.download import Downloader, DownloadConfig, DownloadInputData, DownloadOutputResult

from .abc import (
  Message,
  Usage,
  ChatResponse,
  ChatClient,
  ToolCall,
)

class ChatGPTResponse(ChatResponse):
  pass

def load_files(
  openai_client: OpenAI,
  file_urls: List[HttpUrl],
) -> List[str]:
  """
  Download files from URLs and upload them to OpenAI's file storage.
  
  Args:
    openai_client (OpenAI): The OpenAI client.
    file_urls (List[HttpUrl]): The URLs of the files to download.
    
  Returns:
    List[str]: The IDs of the uploaded files.
  """
  file_ids = []
  
  with tempfile.TemporaryDirectory() as temp_dir:
    # Download files
    downloaded: DownloadOutputResult = Downloader(DownloadConfig(
      output_dir=temp_dir,
    )).process(DownloadInputData(
      urls=[str(url) for url in file_urls],
    ))
    
    # Upload files to OpenAI's file storage
    for i, dl in enumerate(downloaded.downloaded_files):
      if not dl:
        raise ValueError(f"Failed to download file from {file_urls[i]}")
      
      file_obj = openai_client.files.create(
        file=open(dl, "rb"),
        purpose="assistants"
      )
      file_ids.append(file_obj.id)
  
  return file_ids

def run_assistant(
  openai_client: OpenAI,
  model: str,
  messages: List[Message],
  **kwargs
) -> ChatGPTResponse:
  """
  Run an assistant with a list of messages.
  
  Args:
    openai_client (OpenAI): The OpenAI client.
    model (str): The model to use.
    messages (List[Message]): The list of messages to send to the assistant.
    **kwargs: Additional arguments for the assistant.
    
  Returns:
    ChatGPTResponse: The response from the assistant.
  """
  adjusted_default_args = {
    "temperature": 1e-6,
    "tools": [{"type": "file_search"}],
  }
  kwargs = {**adjusted_default_args, **kwargs}
  
  thread = None
  assistant = None
  
  try:
    instructions = ""
    
    thread_messages = []
    for message in messages:
      # Take only the last system message as instructions
      if message.role == "system":
        instructions = message.content
        continue
      
      if not message.files:
        thread_messages.append(message.model_dump(
          mode="json", exclude_none=True, exclude_unset=True, exclude=["files"],
        ))
        continue
      
      # Load files
      file_ids = load_files(openai_client, message.files)
      thread_messages.append(message.model_dump(
        mode="json", exclude_none=True, exclude_unset=True, exclude=["files"],
      ) | {
        "attachments": [{
          "file_id": id,
          "tools": [{"type": "file_search"}],
        } for id in file_ids],
      })
      
    # Create assistant
    assistant = openai_client.beta.assistants.create(
      model=model,
      instructions=instructions,
      **kwargs
    )
    
    # Create thread
    thread = openai_client.beta.threads.create()
    
    # Add messages to thread
    for message in thread_messages:
      openai_client.beta.threads.messages.create(
        thread_id=thread.id,
        **message,
      )
      
    # Create run
    run = openai_client.beta.threads.runs.create_and_poll(
      assistant_id=assistant.id,
      thread_id=thread.id,
      **kwargs,
    )
    
    # Return response
    result_messages = list(openai_client.beta.threads.messages.list(
      thread_id=thread.id, run_id=run.id,
    ))
    
    content = ""
    if isinstance(result_messages, list) and len(result_messages) > 0:
      content = result_messages[0].content[0].text.value
    
    return ChatGPTResponse(
      role="assistant",
      content=content,
      usage=Usage.model_validate(run.usage.model_dump(
        mode="json", exclude_none=True, exclude_unset=True,
      ) | {"model": run.model}),
    )
      
  finally:
    if thread and isinstance(thread, Thread):
      openai_client.beta.threads.delete(thread.id)
    if assistant and isinstance(assistant, Assistant):
      openai_client.beta.assistants.delete(assistant.id)

class ChatGPTClient(ChatClient):
  def __init__(self):
    self.openai_client = OpenAI()
    
  @classmethod
  def tool_result_to_message(
    cls,
    tool_call: ToolCall,
    tool_result: str,
    **_
  ) -> Message:
    return Message(
      role="tool",
      content=json.dumps({
        **json.loads(tool_call.function.arguments),
        "result": tool_result,
      }, ensure_ascii=False),
      tool_call_id=tool_call.id,
    )
    
  @classmethod
  def cook_message(cls, message: Message) -> Dict[str, Any]:
    cooked = message.model_dump(
      mode="json", exclude_none=True, exclude_unset=True,
    )
    
    if message.image is not None:
      cooked["content"] = [{
        "type": "text",
        "text": message.content or "",
      }, {
        "type": "image_url",
        "image_url": {"url": str(message.image)},
      }]
      
    #TODO Processing audio content
      
    return cooked
  
  def complete_chat(
    self,
    messages: List[Message],
    model: str,
    stream: bool = False,
    temperature: float = 0.0,
    tools: Optional[List[Dict[str, Any]]] = None,
    tool_choice: Optional[str|Dict[str, Any]] = None,
    **kwargs
  ) -> ChatGPTResponse:
    # Check if files are attached
    has_files = False
    for message in messages:
      if message.files and isinstance(message.files, list):
        has_files = True
        break
    
    if has_files:
      # Call run_assistant
      return run_assistant(
        self.openai_client,
        model,
        messages,
        **kwargs
      )
    
    chat_completion: ChatCompletion = self.openai_client.chat.completions.create(
      model=model,
      messages=[self.cook_message(message) for message in messages],
      stream=stream,
      temperature=temperature,
      tools=tools,
      tool_choice=tool_choice,
      **kwargs
    )
    
    response_message = chat_completion.choices[0].message.model_dump(mode="json")
    usage = chat_completion.usage.model_dump(mode="json")
    
    return ChatGPTResponse(
      **{
        **response_message,
        "usage": {**usage, "model": chat_completion.model},
      }
    )