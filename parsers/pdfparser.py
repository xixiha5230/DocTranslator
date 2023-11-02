import threading
from io import BytesIO

import pdfplumber
import tqdm
from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

from runner.run import Runner
from translator.translator import Translator


class PdfParser:
    def __init__(self, in_path, out_path) -> None:
        pdfmetrics.registerFont(TTFont("SimSun", "./fonts/SIMSUN.TTC"))
        self.translator = Translator()
        self.lock = threading.Lock()
        self.runner = Runner()
        self.canvas = Canvas(out_path)
        self.in_path = in_path
        self.out_path = out_path

    def run(self):
        with pdfplumber.open(self.in_path) as in_pdf:
            for i in tqdm.tqdm(range(len(in_pdf.pages))):
                self.page = in_pdf.pages[i]
                self.canvas.setPageSize((self.page.width, self.page.height))
                self.canvas.setFont("SimSun", 6)
                self.canvas.setFillColorRGB(0, 0, 0)
                elements = (
                    self.page.extract_words()
                    + self.page.extract_tables()
                    + self.page.images
                )

                self.runner.run(self.process_element, elements)

                self.canvas.showPage()
            self.canvas.save()
        in_pdf.close()

    def process_element(self, element):
        if "text" in element and element["text"] != " ":
            trans = self.translator.cn2en(element["text"])
            with self.lock:
                self.canvas.drawString(
                    float(element["x0"]),
                    float(self.page.height - element["top"]),
                    trans,
                )
        elif isinstance(element, list):
            pass
        else:
            try:
                img = element["stream"].get_data()
                img_pil = Image.open(BytesIO(img))
                img = ImageReader(img_pil)
                with self.lock:
                    self.canvas.drawImage(
                        img,
                        float(element["x0"]),
                        element["y0"],
                        element["width"],
                        element["height"],
                    )
            except:
                pass
