import re

from googletrans import Translator as T


class Translator:
    def __init__(self) -> None:
        self.translator = T(service_urls=["translate.google.com"])

    def _is_contain_chinese(self, word):
        pattern = re.compile(r"[\u4e00-\u9fa5]")
        match = pattern.search(word)
        return True if match else False

    def cn2en(self, text):
        if not self._is_contain_chinese(text):
            return text
        else:
            try:
                trans = self.translator.translate(text, src="zh-cn", dest="en")
                return trans.text
            except:
                print(text)
                return text
