# med-chat

A framework of LLM chat clients for mediq applications.

## Install

`pip install med-chat`

## Usage

```python
from med_chat import Message, ChatClient

chat_client = ChatClient.use("chatgpt")
response = chat_client.complete_chat(
  messages = [
    Message(role="user", content="What is the capital of the United States?"),
  ],
  model="gpt-3.5-turbo"
)
print(response)
```

See more examples under `tests` directory.
