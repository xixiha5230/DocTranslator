# 文档翻译

## 简介
可以将word文档中的中文翻译为英文，支持多种翻译器，包括谷歌翻译、火山翻译、GPT翻译。

## 配置文件
配置文件位于`config/setting.cfg`
### gpt
- `"openai-apikey = sk-"` 为openai的apikey，需要自行申请，申请地址：https://beta.openai.com/ ，申请后将apikey填入配置文件中。
- `"openai-proxy = "` 为openai的代理，如果不需要代理，可以不填写。
- `"prompt = "` 为openai的prompt，可以自行修改，但是需要保留`Translate Chinese to English:`，因为程序会根据这个字符串来判断是否需要翻译。 
### volc
- `"k_access_key = "` 火山引擎的access key, 从 https://translate.volcengine.com/api 免费获取
- `"k_secret_key = "` 同上一起获取


## 启动
```python
python main.py --input SOP.docx --output out.docx --translator google
```

## 参数说明
- `--input` 输入文件路径
- `--output` 输出文件路径
- `--translator` 翻译器，可选值：`google`、`volc`、`gpt`，默认为`google`
