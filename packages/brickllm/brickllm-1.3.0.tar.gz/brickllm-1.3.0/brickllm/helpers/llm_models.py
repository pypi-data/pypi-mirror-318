from typing import Union

from langchain.chat_models.base import BaseChatModel
from langchain_anthropic import ChatAnthropic
from langchain_community.llms import Ollama
from langchain_fireworks import ChatFireworks
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


def _get_model(model: Union[str, BaseChatModel]) -> BaseChatModel:
    """
    Get the LLM model based on the provided model type.

    Args:
        model (Union[str, BaseChatModel]): The model type as a string or an instance of BaseChatModel.

    Returns:
        BaseChatModel: The LLM model instance.
    """

    if isinstance(model, BaseChatModel):
        return model

    if model == "openai":
        return ChatOpenAI(temperature=0, model="gpt-4o")
    elif model == "ollama3.2":
        return ChatOllama(model="llama3.2")
    elif model == "anthropic":
        return ChatAnthropic(temperature=0, model_name="claude-3-sonnet-20240229")
    elif model == "fireworks":
        return ChatFireworks(
            temperature=0, model="accounts/fireworks/models/llama-v3p1-70b-instruct"
        )
    elif model == "llama3.1:8b-brick":
        return Ollama(model="llama3.1:8b-brick-v8")
    elif model == "llama32-3B-brick":
        return Ollama(model="hf.co/Giudice7/llama32-3B-brick-demo:latest")

    else:
        raise ValueError(
            f"Unsupported model type: {model}. Load your own BaseChatModel if this one is not supported."
        )
