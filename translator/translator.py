import configparser
import logging
import re
from cgitb import text
from tkinter import NO, E


class Translator:
    def __init__(self) -> None:
        self.map = {}

    def _read_config(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        with open("./config/settings.cfg") as f:
            config_text = f.read()
            config.read_string(config_text)
        return config

    def _is_contain_chinese(self, word):
        pattern = re.compile(r"[\u4e00-\u9fa5]")
        match = pattern.search(word)
        return True if match else False

    def _get_cache(self, text):
        if self.map.__contains__(text):
            return self.map[text]
        else:
            return None

    def _cache(self, cn_text, en_text):
        if not self.map.__contains__(text):
            self.map[cn_text] = en_text

    def _cn2en(self, text):
        raise NotImplemented

    def cn2en(self, text):
        if not self._is_contain_chinese(text):
            return text
        if self._get_cache(text) is not None:
            return self._get_cache(text)
        try:
            en_text = self._cn2en(text)
            self._cache(text, en_text)
            text = en_text
        except Exception as e:
            logging.error(f"{text} translate error: {e}")
        return text
