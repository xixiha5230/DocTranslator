import argparse
import importlib
import os

file_type_to_parser = {
    ".pdf": "parsers.pdfparser.PdfParser",
    ".docx": "parsers.docxparser.DocxParser",
}

translator_type_to_translator = {
    "gpt": "translator.gpt.GPTTranslator",
    "google": "translator.google.GoogleTranslator",
}


def _get_class(full_path: str):
    module_name, class_name = full_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--input", help="Input file path", required=True)
    parser.add_argument("--output", help="Output file path", required=True)
    parser.add_argument("--translator", help="Translator type", required=True)
    args = parser.parse_args()
    out_path = args.output
    in_path = args.input
    translator = args.translator

    file_extension = os.path.splitext(in_path)[1]
    translator_type = translator.lower()
    Parser = _get_class(file_type_to_parser[file_extension])
    Translator = _get_class(translator_type_to_translator[translator_type])

    parser = Parser(in_path, out_path, Translator())
    parser.run()
