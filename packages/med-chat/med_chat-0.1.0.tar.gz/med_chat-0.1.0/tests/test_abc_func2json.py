from med_chat import ChatClient

def test_basic_func():
  def basic_func(a: int, b: int) -> int:
    return a + b
  
  json_dict = ChatClient.func2json(basic_func)
  assert json_dict == {
    "type": "function",
    "function": {
      "name": "basic_func",
      "description": "",
      "parameters": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer",
            "description": "",
          },
          "b": {
            "type": "integer",
            "description": "",
          },
        },
        "required": ["a", "b"],
      },
    },
  }
  
def test_complex_func():
  def complex_func(a: int, b: int, c: str = "default") -> dict:
    """
    This is a complex function.
    
    Args:
      a (int): The first argument.
      b (int): The second argument.
      c (str): The third argument.
    """
    return {
      "a": a,
      "b": b,
      "c": c,
    }
  
  json_dict = ChatClient.func2json(complex_func)
  assert json_dict == {
    "type": "function",
    "function": {
      "name": "complex_func",
      "description": "This is a complex function.",
      "parameters": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer",
            "description": "The first argument.",
          },
          "b": {
            "type": "integer",
            "description": "The second argument.",
          },
          "c": {
            "type": "string",
            "description": "The third argument.",
          },
        },
        "required": ["a", "b"],
      },
    },
  }