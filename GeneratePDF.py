from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont

import BarcodeGeneration


def generate_img_from_pdf():
    pages = convert_from_path('pdf-test.pdf', size=(1200, 1800), poppler_path=r"C:\poppler-23.01.0\Library\bin")
    for page in pages:
        page.save('out3.jpg', 'JPEG')


def generating_img_with_barcode():
    # Open the image
    img = Image.open("out3.jpg")

    # Resize the image
    width, height = img.size
    new_width = width - 120  # leave 100 pixels of space in the upper right corner
    new_height = height - 180  # leave 100 pixels of space in the upper right corner
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    newIMG = Image.new("RGB", (1200, 1800), (255, 255, 255))
    newIMG.paste(img, (0, 0))
    lineIMG = Image.open("line.png")
    newIMG.paste(lineIMG, (0, 0))
    barcode = Image.open("barcode.png")
    barcodeValue = BarcodeGeneration.read_barcode('barcode.png')
    imgBarcodeValue = Image.new("RGB", (100, 50), "white")
    draw = ImageDraw.Draw(imgBarcodeValue)
    font = ImageFont.truetype("arial.ttf", 16)
    draw.text((10, 10), barcodeValue, fill=(0, 0, 0), font=font)
    # generate an image with barcodeValue which is a string
    newIMG.paste(imgBarcodeValue, (0, 0))
    newIMG.paste(barcode, (900, 0))
    newIMG.save("out4.jpg")
    generate_img_from_pdf()


def generate_pdf_from_img():
    pdf = Image.open("out4.jpg")
    pdf.save("out4.pdf")

if __name__ == '__main__':
    generate_img_from_pdf()
    generating_img_with_barcode()
