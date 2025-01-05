import json
from typing import Literal

from med_chat import ChatClient, Message

def test_complete_chat():
  chat_client = ChatClient.use("chatgpt")
  response = chat_client.complete_chat(
    messages=[
      Message(
        role="user",
        content="What is the capital of the United States?",
      ),
    ],
    model="gpt-3.5-turbo",
  )
  print(response)
  
  assert response.role == "assistant"
  assert "Washington, D.C." in response.content
  assert "gpt-3.5-turbo" in response.usage.model
  assert response.usage.total_tokens == response.usage.prompt_tokens + response.usage.completion_tokens
  assert response.tool_calls is None
  
def test_chat_with_image():
  img_url = "https://www.mdpi.com/cancers/cancers-13-03704/article_deploy/html/images/cancers-13-03704-g001.png"
  
  chat_client = ChatClient.use("chatgpt")
  response = chat_client.complete_chat(
    messages=[
      Message(
        role="user",
        content="Can you explain this image?",
        image=img_url,
      ),
    ],
    model="gpt-4o",
  )
  print(response)
  
  assert response.role == "assistant"
  assert "ALK fusion protein" in response.content
  assert "gpt-4o" in response.usage.model
  assert response.usage.total_tokens == response.usage.prompt_tokens + response.usage.completion_tokens
  assert response.tool_calls is None

def test_chat_with_tool_calls():
  def get_weather(location: str, unit: Literal["c", "f"]="c") -> str:
    if unit == "c":
      return f"The weather in {location} is 25°C."
    elif unit == "f":
      return f"The weather in {location} is 77°F."
    else:
      raise ValueError("Invalid unit.")

  chat_client = ChatClient.use("chatgpt")
  response = chat_client.complete_chat(
    messages=[
      Message(
        role="user",
        content="What is the weather in New York today?",
      ),
    ],
    model="gpt-4o",
    tools=[chat_client.func2json(get_weather)],
    tool_choice="auto",
  )
  print(response)
  assert response.tool_calls is not None
  
  # Call the function
  tool_call = response.tool_calls[0]
  assert tool_call.function.name == "get_weather"
  
  arguments = json.loads(tool_call.function.arguments)
  result = get_weather(**arguments)
  
  # Simulate the messages after the tool call
  messages = [
    Message(
      role="user",
      content="What is the weather in New York today?",
    ),
    Message(
      **response.model_dump(mode="json", exclude_none=True, exclude_unset=True),
    ),
    chat_client.tool_result_to_message(tool_call, result),
  ]
  print(messages)
  
  response = chat_client.complete_chat(
    messages=messages,
    model="gpt-4o",
  )
  print(response)
  assert response.role == "assistant"
  assert "New York" in response.content and "25°C" in response.content
  assert response.tool_calls is None
  assert response.usage.total_tokens == response.usage.prompt_tokens + response.usage.completion_tokens
  
def test_chat_with_files():
  file_url = "https://smartmediq-public.s3.us-east-1.amazonaws.com/13195_2021_Article_813.pdf"
  
  chat_client = ChatClient.use("chatgpt")
  response = chat_client.complete_chat(
    messages=[
      Message(
        role="system",
        content="""Summarize the clinical trial research paper in a concise format with the following points:
        
        1. Background: Briefly describe the problem or question the study addresses.
        2. Methods: Summarize the study design, population, interventions, and key methods used.
        3. Results: Highlight the major findings, including any statistical significance and relevant outcomes.
        4. Conclusions: Summarize the key takeaways and implications of the study.
        
        Ensure the summary is precise and captures the essence of the research without unnecessary details.
        """,  
      ),
      Message(
        role="user",
        content="Please summarize the attached document.",
        files=[file_url],
      ),
    ],
    model="gpt-4o",
  )
  print(response)
  
  assert response.role == "assistant"
  assert "Background" in response.content and "Methods" in response.content and "Results" in response.content and "Conclusions" in response.content
  assert "gpt-4o" in response.usage.model
  assert response.usage.total_tokens == response.usage.prompt_tokens + response.usage.completion_tokens
  assert response.tool_calls is None