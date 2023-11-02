import time

from googletrans import Translator as T

from translator.translator import Translator


class GoogleTranslator(Translator):
    def __init__(self) -> None:
        super().__init__()
        self.translator = T(service_urls=["translate.google.com"])

    def _cn2en(self, text) -> str:
        trans = self.translator.translate(text, src="zh-cn", dest="en")
        time.sleep(0.3)
        return trans.text
