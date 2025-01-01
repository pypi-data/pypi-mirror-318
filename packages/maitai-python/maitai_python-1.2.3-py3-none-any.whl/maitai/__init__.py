import os

from maitai._azure import MaitaiAsyncAzureOpenAIClient, MaitaiAzureOpenAIClient
from maitai._context import ContextManager
from maitai._evaluator import Evaluator as Evaluator
from maitai._inference import Inference as Inference
from maitai._maitai import Chat, Maitai
from maitai._maitai_async import MaitaiAsync

chat = Chat()
context = ContextManager()
AsyncOpenAI = MaitaiAsync
OpenAI = Maitai

AsyncAzureOpenAI = MaitaiAsyncAzureOpenAIClient
AzureOpenAI = MaitaiAzureOpenAIClient


def initialize(api_key):
    from maitai._config import config

    config.initialize(api_key)
