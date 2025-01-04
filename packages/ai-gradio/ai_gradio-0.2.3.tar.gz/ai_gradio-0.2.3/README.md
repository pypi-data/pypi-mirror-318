# `ai-gradio`

A Python package that makes it easy for developers to create machine learning apps powered by OpenAI, Google's Gemini models, Anthropic's Claude, LumaAI, CrewAI, XAI's Grok, and Hyperbolic and more.

## Installation

You can install `ai-gradio` with different providers:

```bash
# Install with OpenAI support
pip install 'ai-gradio[openai]'

# Install with Gemini support  
pip install 'ai-gradio[gemini]'

# Install with CrewAI support
pip install 'ai-gradio[crewai]'

# Install with Anthropic support
pip install 'ai-gradio[anthropic]'

# Install with LumaAI support
pip install 'ai-gradio[lumaai]'

# Install with XAI support
pip install 'ai-gradio[xai]'

# Install with Cohere support
pip install 'ai-gradio[cohere]'

# Install with SambaNova support
pip install 'ai-gradio[sambanova]'

# Install with Hyperbolic support
pip install 'ai-gradio[hyperbolic]'

# Install with all providers
pip install 'ai-gradio[all]'

# Installation additions:
pip install 'ai-gradio[fireworks]'
pip install 'ai-gradio[together]'
pip install 'ai-gradio[qwen]'

# Install with DeepSeek support
pip install 'ai-gradio[deepseek]'

# Install with SmolagentsAI support
pip install 'ai-gradio[smolagents]'

# Install with Groq support
pip install 'ai-gradio[groq]'
```

## Basic Usage

First, set your API key in the environment:

For OpenAI:
```bash
export OPENAI_API_KEY=<your token>
```

For Gemini:
```bash
export GEMINI_API_KEY=<your token>
```

For Anthropic:
```bash
export ANTHROPIC_API_KEY=<your token>
```

For LumaAI:
```bash
export LUMAAI_API_KEY=<your token>
```

For XAI:
```bash
export XAI_API_KEY=<your token>
```

For Cohere:
```bash
export COHERE_API_KEY=<your token>
```

For SambaNova:
```bash
export SAMBANOVA_API_KEY=<your token>
```

For Hyperbolic:
```bash
export HYPERBOLIC_API_KEY=<your token>
```

For DeepSeek:
```bash
export DEEPSEEK_API_KEY=<your token>
```

Then in a Python file:

```python
import gradio as gr
import ai_gradio

# Create a Gradio interface
gr.load(
    name='openai:gpt-4-turbo',  # or 'gemini:gemini-1.5-flash' for Gemini, or 'xai:grok-beta' for Grok
    src=ai_gradio.registry,
    title='AI Chat',
    description='Chat with an AI model'
).launch()
```

## Features

### Text Chat
Basic text chat is supported for all text models. The interface provides a chat-like experience where you can have conversations with the AI model.

### Voice Chat (OpenAI only)
Voice chat is supported for OpenAI realtime models. You can enable it in two ways:

```python
# Using a realtime model
gr.load(
    name='openai:gpt-4o-realtime-preview-2024-10-01',
    src=ai_gradio.registry
).launch()

# Or explicitly enabling voice chat with any realtime model
gr.load(
    name='openai:gpt-4o-mini-realtime-preview-2024-12-17',
    src=ai_gradio.registry,
    enable_voice=True
).launch()
```

### Voice Chat Configuration

For voice chat functionality, you'll need:

1. OpenAI API key (required):
```bash
export OPENAI_API_KEY=<your OpenAI token>
```

2. Twilio credentials (recommended for better WebRTC performance):
```bash
export TWILIO_ACCOUNT_SID=<your Twilio account SID>
export TWILIO_AUTH_TOKEN=<your Twilio auth token>
```

You can get Twilio credentials by:
- Creating a free account at Twilio
- Finding your Account SID and Auth Token in the Twilio Console

Without Twilio credentials, voice chat will still work but might have connectivity issues in some network environments.

### Gemini Code Generator Interface
```python
import gradio as gr
import ai_gradio

# Create a code generation interface with Gemini
gr.load(
    name='gemini:gemini-pro',
    src=ai_gradio.registry,
    coder=True,  # Enable code generation interface
    title='Gemini Code Generator',
    description='Generate web applications with Gemini'
).launch()
```

This creates an interactive code generation interface with:
- Input area for describing the desired web application
- Live preview of generated code
- Example templates
- System prompt configuration
- Code history tracking
- Real-time code preview

Example prompts:
```python
examples = [
    "Create a button that changes color when clicked",
    "Create a simple todo list with add/remove functionality",
    "Create a countdown timer with start/pause/reset controls"
]
```

### Video Chat (Gemini only)
Video chat is supported for Gemini models. You can enable it by setting `enable_video=True`:

```python
gr.load(
    name='gemini:gemini-1.5-flash',
    src=ai_gradio.registry,
    enable_video=True
).launch()
```

### Text Generation with DeepSeek
DeepSeek models support text generation and coding assistance:

```python
gr.load(
    name='deepseek:deepseek-chat',
    src=ai_gradio.registry,
    title='DeepSeek Chat',
    description='Chat with DeepSeek'
).launch()

# For code assistance
gr.load(
    name='deepseek:deepseek-coder',
    src=ai_gradio.registry,
    title='DeepSeek Coder',
    description='Get coding help from DeepSeek'
).launch()

# For vision tasks
gr.load(
    name='deepseek:deepseek-vision',
    src=ai_gradio.registry,
    title='DeepSeek Vision',
    description='Visual understanding with DeepSeek'
).launch()
```

### Text Generation with Anthropic Claude
Anthropic's Claude models are supported for text generation:

```python
gr.load(
    name='anthropic:claude-3-opus-20240229',
    src=ai_gradio.registry,
    title='Claude Chat',
    description='Chat with Claude'
).launch()
```

### AI Video and Image Generation with LumaAI
LumaAI support allows you to generate videos and images from text prompts:

```python
# For video generation
gr.load(
    name='lumaai:dream-machine',
    src=ai_gradio.registry,
    title='LumaAI Video Generation'
).launch()

# For image generation
gr.load(
    name='lumaai:photon-1',
    src=ai_gradio.registry,
    title='LumaAI Image Generation'
).launch()
```

### Text Generation with Hyperbolic
Hyperbolic models support various LLMs including DeepSeek, LLaMA, and Qwen:

```python
# Using DeepSeek V3
gr.load(
    name='hyperbolic:deepseek-ai/DeepSeek-V3',
    src=ai_gradio.registry,
    title='DeepSeek Chat',
    description='Chat with DeepSeek V3'
).launch()

# Using LLaMA 3.3
gr.load(
    name='hyperbolic:meta-llama/llama-3.3-70b',
    src=ai_gradio.registry,
    title='LLaMA Chat',
    description='Chat with LLaMA 3.3'
).launch()

# Using Qwen Coder
gr.load(
    name='hyperbolic:Qwen/qwen2.5-coder-32b',
    src=ai_gradio.registry,
    title='Qwen Coder',
    description='Get coding help from Qwen'
).launch()
```

### smolagents

smolagents support provides an intelligent assistant with web search capabilities:

```python
gr.load(
    name='smolagents:meta-llama/Llama-3.1-8B-Instruct',
    src=ai_gradio.registry,
    title='smolagents Assistant',
    description='Agent Assistant'
).launch()
```

The SmolagentsAI integration includes:
- Interactive code generation
- Web search integration via DuckDuckGo
- Step-by-step thought process visibility
- Error handling and debugging assistance
- Real-time streaming responses

### SmolagentsAI Models
- meta-llama/Llama-3.1-8B-Instruct
- meta-llama/Llama-3.1-70B-Instruct
- meta-llama/Llama-3.2-70B-Instruct

### AI Agent Teams with CrewAI
CrewAI support allows you to create teams of AI agents that work together to solve complex tasks. Enable it by using the CrewAI provider:

```python
gr.load(
    name='crewai:gpt-4-turbo',
    src=ai_gradio.registry,
    title='AI Team Chat',
    description='Chat with a team of specialized AI agents'
).launch()
```

### CrewAI Types
The CrewAI integration supports different specialized agent teams:

- `support`: A team of support agents that help answer questions, including:
  - Senior Support Representative
  - Support Quality Assurance Specialist

- `article`: A team of content creation agents, including:
  - Content Planner
  - Content Writer
  - Editor

You can specify the crew type when creating the interface:

```python
gr.load(
    name='crewai:gpt-4-turbo',
    src=ai_gradio.registry,
    crew_type='article',  # or 'support'
    title='AI Writing Team',
    description='Create articles with a team of AI agents'
).launch()
```

When using the `support` crew type, you can provide a documentation URL that the agents will reference when answering questions. The interface will automatically show a URL input field.

### Provider Selection

When loading a model, you can specify the provider explicitly using the format `provider:model_name`. 
```python
# Explicit provider
gr.load(
    name='gemini:gemini-pro',
    src=ai_gradio.registry
).launch()
```

### Customization

You can customize the interface by adding examples, changing the title, or adding a description:

```python
gr.load(
    name='gpt-4-turbo',
    src=ai_gradio.registry,
    title='Custom AI Chat',
    description='Chat with an AI assistant',
    examples=[
        "Explain quantum computing to a 5-year old",
        "What's the difference between machine learning and AI?"
    ]
).launch()
```

### Composition

You can combine multiple models in a single interface using Gradio's Blocks:

```python
import gradio as gr
import ai_gradio

with gr.Blocks() as demo:
    with gr.Tab("GPT-4"):
        gr.load('gpt-4-turbo', src=ai_gradio.registry)
    with gr.Tab("Gemini"):
        gr.load('gemini-pro', src=ai_gradio.registry)
    with gr.Tab("Claude"):
        gr.load('anthropic:claude-3-opus-20240229', src=ai_gradio.registry)
    with gr.Tab("LumaAI"):
        gr.load('lumaai:dream-machine', src=ai_gradio.registry)
    with gr.Tab("CrewAI"):
        gr.load('crewai:gpt-4-turbo', src=ai_gradio.registry)
    with gr.Tab("Grok"):
        gr.load('xai:grok-beta', src=ai_gradio.registry)

demo.launch()
```

## Supported Models

### OpenAI Models
- gpt-4-turbo
- gpt-4
- gpt-3.5-turbo

### Gemini Models
- gemini-pro
- gemini-pro-vision
- gemini-2.0-flash-exp

### Anthropic Models
- claude-3-opus-20240229
- claude-3-sonnet-20240229
- claude-3-haiku-20240307
- claude-2.1
- claude-2.0
- claude-instant-1.2

### LumaAI Models
- dream-machine (video generation)
- photon-1 (image generation)
- photon-flash-1 (fast image generation)

### CrewAI Models
- crewai:gpt-4-turbo
- crewai:gpt-4
- crewai:gpt-3.5-turbo

### XAI Models
- grok-beta
- grok-vision-beta

### Cohere Models
- command
- command-light
- command-nightly
- command-r

### SambaNova Models
- llama2-70b-chat
- llama2-13b-chat
- llama2-7b-chat
- mixtral-8x7b-chat
- mistral-7b-chat

### Fireworks Models
- whisper-v3
- whisper-v3-turbo
- f1-preview
- f1-mini

### Together Models
- meta-llama/Llama-Vision-Free
- meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo
- meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo
- meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
- meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo
- meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo
- meta-llama/Meta-Llama-3-8B-Instruct-Turbo
- meta-llama/Meta-Llama-3-70B-Instruct-Turbo
- meta-llama/Llama-3.2-3B-Instruct-Turbo
- meta-llama/Meta-Llama-3-8B-Instruct-Lite
- meta-llama/Meta-Llama-3-70B-Instruct-Lite

### Qwen Models
- qwen-turbo-latest
- qwen-turbo
- qwen-plus
- qwen-max
- qwen1.5-110b-chat
- qwen1.5-72b-chat
- qwen1.5-32b-chat
- qwen1.5-14b-chat
- qwen1.5-7b-chat
- qwq-32b-preview
- qvq-72b-preview

### Hyperbolic Models
- meta-llama/llama-3.3-70b
- Qwen/QwQ-32B-Preview
- Qwen/qwen2.5-coder-32b
- meta-llama/llama-3.2-3b
- Qwen/qwen2.5-72b
- deepseek/deepseek-v2.5
- meta-llama/llama-3-70b
- hermes/hermes-3-70b
- meta-llama/llama-3.1-405b
- meta-llama/llama-3.1-70b
- meta-llama/llama-3.1-8b

### DeepSeek Models
- deepseek-chat
- deepseek-coder
- deepseek-vision

## Requirements

- Python 3.10 or higher
- gradio >= 5.9.1

Additional dependencies are installed based on your chosen provider:
- OpenAI: `openai>=1.58.1`
- Gemini: `google-generativeai`
- CrewAI: `crewai>=0.1.0`, `langchain>=0.1.0`, `langchain-openai>=0.0.2`, `crewai-tools>=0.0.1`
- Anthropic: `anthropic>=1.0.0`
- LumaAI: `lumaai>=0.0.3`
- XAI: `xai>=0.1.0`
- Cohere: `cohere>=5.0.0`
- DeepSeek: `openai>=1.58.1`
- Hyperbolic: `openai>=1.58.1`

### Fireworks: `openai>=1.58.1`
### Together: `openai>=1.58.1`
### Qwen: `openai>=1.58.1`
### Hyperbolic: `openai>=1.58.1`

## Troubleshooting

If you get a 401 authentication error, make sure your API key is properly set. You can set it manually in your Python session:

```python
import os

# For OpenAI
os.environ["OPENAI_API_KEY"] = "your-api-key"

# For Gemini
os.environ["GEMINI_API_KEY"] = "your-api-key"

# For Anthropic
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

# For LumaAI
os.environ["LUMAAI_API_KEY"] = "your-api-key"

# For XAI
os.environ["XAI_API_KEY"] = "your-api-key"

# For Cohere
os.environ["COHERE_API_KEY"] = "your-api-key"

# For SambaNova
os.environ["SAMBANOVA_API_KEY"] = "your-api-key"

# Environment variables additions:
export FIREWORKS_API_KEY=<your token>
export TOGETHER_API_KEY=<your token>
export QWEN_API_KEY=<your token>
export HYPERBOLIC_API_KEY=<your token>

# Additional troubleshooting environment variables:
os.environ["FIREWORKS_API_KEY"] = "your-api-key"
os.environ["TOGETHER_API_KEY"] = "your-api-key"
os.environ["QWEN_API_KEY"] = "your-api-key"
os.environ["HYPERBOLIC_API_KEY"] = "your-api-key"
os.environ["DEEPSEEK_API_KEY"] = "your-api-key"

### No Providers Error
If you see an error about no providers being installed, make sure you've installed the package with the desired provider:

```bash
# Install with OpenAI support
pip install 'ai-gradio[openai]'

# Install with Gemini support
pip install 'ai-gradio[gemini]'

# Install with CrewAI support
pip install 'ai-gradio[crewai]'

# Install with Anthropic support
pip install 'ai-gradio[anthropic]'

# Install with LumaAI support
pip install 'ai-gradio[lumaai]'

# Install with XAI support
pip install 'ai-gradio[xai]'

# Install with Cohere support
pip install 'ai-gradio[cohere]'

# Install all providers
pip install 'ai-gradio[all]'
```

## Optional Dependencies

For voice chat functionality:
- gradio-webrtc
- numba==0.60.0
- pydub
- librosa
- websockets
- twilio
- gradio_webrtc[vad]
- numpy

For video chat functionality:
- opencv-python
- Pillow

## Examples

### Basic Chat Interface
```python
import gradio as gr
import ai_gradio

# Simple chat with GPT-4
gr.load(
    name='openai:gpt-4-turbo',
    src=ai_gradio.registry,
    title='GPT-4 Chat',
    description='Chat with GPT-4'
).launch()
```

### Multi-Model Interface
```python
import gradio as gr
import ai_gradio

with gr.Blocks() as demo:
    gr.Markdown("# AI Model Hub")
    
    with gr.Tab("Text Models"):
        with gr.Tab("GPT-4"):
            gr.load('openai:gpt-4-turbo', src=ai_gradio.registry)
        with gr.Tab("Claude"):
            gr.load('anthropic:claude-3-opus-20240229', src=ai_gradio.registry)
        with gr.Tab("DeepSeek"):
            gr.load('deepseek:deepseek-chat', src=ai_gradio.registry)
            
    with gr.Tab("Vision Models"):
        with gr.Tab("Gemini Vision"):
            gr.load('gemini:gemini-pro-vision', src=ai_gradio.registry, enable_video=True)
        with gr.Tab("LumaAI"):
            gr.load('lumaai:dream-machine', src=ai_gradio.registry)
            
    with gr.Tab("Specialized"):
        with gr.Tab("Code Assistant"):
            gr.load('deepseek:deepseek-coder', src=ai_gradio.registry)
        with gr.Tab("AI Team"):
            gr.load('crewai:gpt-4-turbo', src=ai_gradio.registry, crew_type='article')

demo.launch()
```

### Voice-Enabled Chat
```python
import gradio as gr
import ai_gradio

# Enable voice chat with GPT-4
gr.load(
    name='openai:gpt-4-turbo',
    src=ai_gradio.registry,
    enable_voice=True,
    title='Voice Chat',
    description='Talk with GPT-4'
).launch()
```

### Custom Examples and Styling
```python
import gradio as gr
import ai_gradio

# Chat interface with custom examples and CSS
gr.load(
    name='gemini:gemini-pro',
    src=ai_gradio.registry,
    title='Gemini Pro Assistant',
    description='Your AI research companion',
    examples=[
        "Explain quantum entanglement",
        "What are the main differences between RNA and DNA?",
        "How does a neural network learn?"
    ],
    css=".gradio-container {background-color: #f0f8ff}"
).launch()
```

### AI Team for Content Creation
```python
import gradio as gr
import ai_gradio

# CrewAI setup for article writing
gr.load(
    name='crewai:gpt-4-turbo',
    src=ai_gradio.registry,
    crew_type='article',
    title='AI Writing Team',
    description='Collaborate with AI agents to create articles',
    examples=[
        "Write a blog post about sustainable energy",
        "Create a technical tutorial about Docker containers"
    ]
).launch()
```

### Support Team with Documentation
```python
import gradio as gr
import ai_gradio

# CrewAI support team with documentation reference
gr.load(
    name='crewai:gpt-4-turbo',
    src=ai_gradio.registry,
    crew_type='support',
    title='AI Support Team',
    description='Get help from AI support agents',
    documentation_url='https://docs.example.com'
).launch()
```

For Groq:
```bash
export GROQ_API_KEY=<your token>
```






