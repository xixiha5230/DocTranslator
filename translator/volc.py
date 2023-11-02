import json
import time

from volcengine.ApiInfo import ApiInfo
from volcengine.base.Service import Service
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo

from translator.translator import Translator


class Volc(Translator):
    def __init__(self):
        super().__init__()
        config = self._read_config()
        k_access_key = config.get("volc", "k_access_key")
        k_secret_key = config.get("volc", "k_secret_key")

        k_service_info = ServiceInfo(
            "translate.volcengineapi.com",
            {"Content-Type": "application/json"},
            Credentials(k_access_key, k_secret_key, "translate", "cn-north-1"),
            5,
            5,
        )
        k_query = {"Action": "TranslateText", "Version": "2020-06-01"}
        k_api_info = {"translate": ApiInfo("POST", "/", k_query, {}, {})}
        self.service = Service(k_service_info, k_api_info)

    def _cn2en(self, text):
        body = {
            "TargetLanguage": "en",
            "TextList": [text],
        }
        res = self.service.json("translate", {}, json.dumps(body))
        t = json.loads(res)["TranslationList"][0]["Translation"]
        time.sleep(0.5)
        return t
