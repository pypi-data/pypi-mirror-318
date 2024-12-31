import os
from openai import OpenAI
import gradio as gr
from typing import Callable


def get_fn(model_name: str, preprocess: Callable, postprocess: Callable, api_key: str, base_url: str = None):
    def fn(message, history):
        inputs = preprocess(message, history)
        # Set base URL and adjust endpoint handling
      
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.hyperbolic.xyz/v1"
        )
            
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                *inputs["messages"]
            ],
            stream=True,
            temperature=0.7,
            max_tokens=512,
            top_p=0.9,
        )
        response_text = ""
        for chunk in completion:
            delta = chunk.choices[0].delta.content or ""
            response_text += delta
            yield postprocess(response_text)

    return fn


def get_interface_args(pipeline):
    if pipeline == "chat":
        inputs = None
        outputs = None

        def preprocess(message, history):
            messages = []
            for user_msg, assistant_msg in history:
                messages.append({"role": "user", "content": user_msg})
                messages.append({"role": "assistant", "content": assistant_msg})
            messages.append({"role": "user", "content": message})
            return {"messages": messages}

        postprocess = lambda x: x  # No post-processing needed
    else:
        # Add other pipeline types when they will be needed
        raise ValueError(f"Unsupported pipeline type: {pipeline}")
    return inputs, outputs, preprocess, postprocess


def get_pipeline(model_name):
    # Determine the pipeline type based on the model name
    # For simplicity, assuming all models are chat models at the moment
    return "chat"


def registry(name: str, token: str | None = None, base_url: str | None = None, **kwargs):
    """
    Create a Gradio Interface for a model on Hyperbolic.

    Parameters:
        - name (str): The name of the model.
        - token (str, optional): The Hyperbolic API key. If not provided, will look for HYPERBOLIC_API_KEY env variable.
        - base_url (str, optional): The base URL for the Hyperbolic API.
    """
    api_key = token or os.environ.get("HYPERBOLIC_API_KEY")
    if not api_key:
        raise ValueError("API key is not set. Please provide a token or set HYPERBOLIC_API_KEY environment variable.")

    pipeline = get_pipeline(name)
    inputs, outputs, preprocess, postprocess = get_interface_args(pipeline)
    fn = get_fn(name, preprocess, postprocess, api_key, base_url)

    if pipeline == "chat":
        interface = gr.ChatInterface(fn=fn, **kwargs)
    else:
        interface = gr.Interface(fn=fn, inputs=inputs, outputs=outputs, **kwargs)

    return interface