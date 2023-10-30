import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO

import pdfplumber
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from translator import Translator

pdfmetrics.registerFont(TTFont("SimSun", "SIMSUN.TTC"))
translator = Translator()
lock = threading.Lock()


def process_element(element, canvas, page):
    if 'text' in element and element['text'] != ' ':
        trans = translator.cn2en(element['text'])
        with lock:
            canvas.drawString(float(element['x0']), float(
                page.height - element['top']), trans)
        print(trans)
    elif isinstance(element, list):
        pass
    else:
        try:
            img = element['stream'].get_data()
            img_pil = Image.open(BytesIO(img))
            img = ImageReader(img_pil)
            with lock:
                canvas.drawImage(img, float(
                    element['x0']), element['y0'], element['width'], element['height'])
        except:
            print("Error")


out_path = "out.pdf"
with pdfplumber.open('SOP.pdf') as in_pdf:
    page_number = 0
    can = canvas.Canvas(out_path, pagesize=letter)

    for page in in_pdf.pages:
        page_number += 1
        print(f"Page {page_number}")

        can.setPageSize((page.width, page.height))
        can.setFont("SimSun", 8)
        can.setFillColorRGB(0, 0, 0)

        elements = page.extract_words() + page.extract_tables() + page.images

        with ThreadPoolExecutor(max_workers=13) as executor:
            futures = [executor.submit(
                process_element, element, can, page) for element in elements]
            for future in as_completed(futures):
                pass

        can.showPage()
    can.save()
in_pdf.close()
