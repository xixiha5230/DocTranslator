import os

import openai

from translator.translator import Translator


class GPTTranslator(Translator):
    def __init__(self) -> None:
        super().__init__()
        self.config = self._read_config()
        self.api_key = self.config.get("gpt", "openai-apikey")
        self.prompt = self.config.get("gpt", "prompt")
        self.proxy = self.config.get("gpt", "openai-proxy")
        if self.prompt != "":
            openai.api_base = os.environ.get("OPENAI_API_BASE", self.proxy)
            print("正在使用OpenAI API 代理，代理地址为: " + openai.api_base)
        openai.api_key = self.api_key

    def _create_chat_completion(self, prompt, text, model="gpt-3.5-turbo", **kwargs):
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}: \n{text}",
                }
            ],
            **kwargs,
        )
        text = (
            completion["choices"][0]
            .get("message")
            .get("content")
            .encode("utf8")
            .decode()
        )
        return text

    def _cn2en(self, text):
        return self._create_chat_completion(self.prompt, text)
