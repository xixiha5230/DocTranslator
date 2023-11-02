import re


class Translator:
    def __init__(self) -> None:
        raise NotImplementedError

    def _is_contain_chinese(self, word):
        pattern = re.compile(r"[\u4e00-\u9fa5]")
        match = pattern.search(word)
        return True if match else False

    def cn2en(self, text):
        raise NotImplementedError
