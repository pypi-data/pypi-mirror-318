#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Time       ：2025/1/1 22:56
# Author     ：Maxwell
# Description：Language Model Management Framework
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, AsyncGenerator


class LanguageModelProperty:
    def __init__(
            self, name: str, short_name: str, company: str, max_input_token: int, max_output_token: int,
            top_p: Optional[float] = None, top_k: Optional[int] = None, temperature: Optional[float] = None,
            timeout: int = 120, input_token_fee_pm: float = 0.0, output_token_fee_pm: float = 0.0,
            train_token_fee_pm: float = 0.0, prompt_version: int = 1, keys: List[str] = []
    ):
        self.name = name
        self.short_name = short_name
        self.company = company
        self.max_input_token = max_input_token
        self.max_output_token = max_output_token
        self.top_p = top_p
        self.top_k = top_k
        self.temperature = temperature
        self.timeout = timeout
        self.input_token_fee_pm = input_token_fee_pm
        self.output_token_fee_pm = output_token_fee_pm
        self.train_token_fee_pm = train_token_fee_pm
        self.prompt_version = prompt_version


class ModelStrategy(ABC):
    @abstractmethod
    async def gen_messages(
            self, question: str, system_prompt: Optional[str] = None, history_messages: Optional[List[Dict]] = None
    ) -> List[Dict[str, str]]:
        pass

    @abstractmethod
    async def chat(self, messages: List[Dict[str, str]]) -> str:
        pass

    @abstractmethod
    async def chat_stream(self, messages: List[Dict[str, str]]) -> AsyncGenerator[str, None]:
        pass


class LanguageModel:

    def __init__(self, strategy: ModelStrategy):
        self._strategy = strategy

    async def chat(
            self, question: str, system_prompt: Optional[str] = None, history_messages: Optional[List[Dict]] = None
    ) -> str:
        messages = await self._strategy.gen_messages(question, system_prompt, history_messages)
        return await self._strategy.chat(messages)

    async def chat_stream(
            self, question: str, system_prompt: Optional[str] = None, history_messages: Optional[List[Dict]] = None
    ) -> AsyncGenerator[str, None]:
        messages = await self._strategy.gen_messages(question, system_prompt, history_messages)
        async for chunk in self._strategy.chat_stream(messages):
            yield chunk

    async def gen_messages(
            self, question: str, system_prompt: Optional[str] = None, history_messages: Optional[List[Dict]] = None
    ) -> List[Dict[str, str]]:
        return await self._strategy.gen_messages(question, system_prompt, history_messages)

    async def chat_with_message(self,  messages: List[Dict[str, str]]) -> str:
        return await self._strategy.chat(messages)

    async def chat_stream_with_message(self, messages: List[Dict[str, str]]) -> AsyncGenerator[str, None]:
        async for chunk in self._strategy.chat_stream(messages):
            yield chunk


class LanguageModelFactory:
    _model_instances: Dict[str, LanguageModel] = {}

    @classmethod
    def register_model_instance(cls, name: str, model_instance: LanguageModel):
        cls._model_instances[name] = model_instance

    @classmethod
    def get_model_instance(cls, name: str) -> Optional[LanguageModel]:
        return cls._model_instances.get(name)

    @classmethod
    def list_models(cls) -> List[str]:
        return list(cls._model_instances)