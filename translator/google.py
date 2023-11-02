from googletrans import Translator as T

from translator.translator import Translator


class GoogleTranslator(Translator):
    def __init__(self) -> None:
        self.translator = T(service_urls=["translate.google.com"])

    def cn2en(self, text) -> str:
        if not self._is_contain_chinese(text):
            return text
        else:
            try:
                trans = self.translator.translate(text, src="zh-cn", dest="en")
                return trans.text
            except:
                print(f"Google Translate Error: {text}")
                return text
