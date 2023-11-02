import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--input", help="Input file path", required=True)
    parser.add_argument("--output", help="Output file path", required=True)
    args = parser.parse_args()
    out_path = args.output
    in_path = args.input
    if in_path.endswith(".pdf") and out_path.endswith(".pdf"):
        from parsers.pdfparser import PdfParser as Parser
    elif in_path.endswith(".docx") and out_path.endswith(".docx"):
        from parsers.docxparser import DocxParser as Parser
    else:
        raise Exception("Invalid file type")
    parser = Parser(in_path, out_path)
    parser.run()
