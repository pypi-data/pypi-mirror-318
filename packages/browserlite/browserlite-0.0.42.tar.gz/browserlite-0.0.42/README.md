# BrowserLite 🌐

BrowserLite is a powerful Python library for browser-based AI chat model interactions, supporting ChatGPT and HuggingChat. It provides a seamless interface for automated browser interactions with popular AI chat services.

[![PyPI version](https://badge.fury.io/py/browserlite.svg)](https://badge.fury.io/py/browserlite)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- 🤖 Easy integration with ChatGPT and HuggingChat
- 🌐 Support for multiple browsers (Chrome, Edge, Firefox)
- 📝 Stream responses in real-time
- 🛠️ Batch processing capabilities
- 🔄 OpenAI-like API interface
- 🔍 Optional web search integration

## 📦 Installation

```bash
pip install browserlite
```

## 🏃‍♂️ Quick Start

### Simple Chat Completion

```python
from browserlite import completion

# Basic usage
response = completion(
    prompt="What is the capital of France?",
    model="chatgpt"  # or "huggingchat"
)
print(response)

# Using with system prompt
response = completion(
    prompt="Explain quantum computing",
    system_prompt="You are a quantum physics expert",
    model="chatgpt"
)
```

### Direct Browser Interface

```python
from browserlite import chatgpt, huggingchat

# Using ChatGPT
response = chatgpt("Write a poem about coding")

# Using HuggingChat
response = huggingchat("Explain machine learning in simple terms")
```

### Streaming Responses

```python
from browserlite import pp_completion

# Print response in real-time
pp_completion(
    prompt="Write a story about AI",
    model="chatgpt",
    stream=True
)
```

### Advanced Usage with Messages

```python
from browserlite import genai

messages = [
    {"role": "system", "content": "You are a helpful coding assistant"},
    {"role": "user", "content": "Write a Python function to sort a list"},
    {"role": "assistant", "content": "Here's a simple sorting function:..."},
    {"role": "user", "content": "Can you add error handling?"}
]

response = genai(
    messages=messages,
    model="chatgpt")
```

### Custom Browser Configuration

```python
from browserlite import AIBrowserClient

client = AIBrowserClient(
    browser='microsoft-edge-stable',  # or 'google-chrome', 'firefox'
    default_sleep=30,
    default_batch_settings={
        "each_chat_start_wait_time": 0,
        "batch_wait_size": 4,
        "batch_wait_time": 10
    }
)

response = client.chat.create(
    messages=[{"role": "user", "content": "Hello!"}],
    model="chatgpt"
)
```

## 🔧 Configuration Options

### Available Models
- `chatgpt`: OpenAI's ChatGPT
- `huggingchat`: HuggingFace's Chat Interface

### Supported Browsers
- `microsoft-edge-stable`
- `google-chrome`
- `firefox`

### Batch Processing Settings
```python
batch_settings = {
    "each_chat_start_wait_time": 0,  # Wait time before each chat
    "batch_wait_size": 4,            # Number of requests before batch wait
    "batch_wait_time": 10            # Wait time between batches
}
```

## 🌟 Advanced Features

### Web Search Integration

```python
response = completion(
    prompt="What's the latest news about AI?",
    web_search=True
)
```

### Streaming with Custom Processing

```python
client = AIBrowserClient()
stream = client.chat.create(
    messages=[{"role": "user", "content": "Tell me a story"}],
    model="chatgpt",
    stream=True
)

for chunk in stream:
    # Process each chunk as it arrives
    content = chunk.choices[0].delta.content
    if content:
        process_chunk(content)
```

### Multiple Formats Support

```python
# String input
response = completion("Hello, how are you?")

# Dictionary format
response = completion({
    "role": "user",
    "content": "Hello!"
})

# List of messages
response = completion([
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi!"}
])
```

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to the Python community
- Special thanks to all contributors

## 🔗 Links
- GitHub: [browserlite](https://github.com/yourusername/browserlite)
- Documentation: [docs](https://browserlite.readthedocs.io)
- PyPI: [browserlite](https://pypi.org/project/browserlite/)