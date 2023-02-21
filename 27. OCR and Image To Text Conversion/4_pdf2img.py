import pytesseract
from pytesseract import Output
import cv2
from pdf2image import convert_from_path


pytesseract.pytesseract.tesseract_cmd = r"/home/hanzala/Development/Python_the_ultimate_course_2023/27. OCR and Image To Text Conversion/tesseract-ocr-w64-setup-5.3.0.20221222.exe"


img = convert_from_path(
    r"/home/hanzala/Development/Python_the_ultimate_course_2023/27. OCR and Image To Text Conversion/Invoice1.pdf")
img = img[0]


text = pytesseract.image_to_string(img)
print(text)

# data = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(data["text"])
