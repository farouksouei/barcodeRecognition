import barcode
from barcode import Code128
from barcode.writer import ImageWriter
import cv2
from pyzbar import pyzbar


def generate_barcode(barcode_value, output_file):
    """Generate barcode of given type and value and save it to given file."""
    barcode_instance = Code128(barcode_value, writer=ImageWriter())
    barcode_instance.default_writer_options['write_text'] = False
    with open(output_file, 'wb') as f:
        barcode_instance.write(f)

    # create a new text file and write the barcode file name in it
    with open('barcode.txt', 'w') as f:
        f.write(output_file)

def read_barcode(barcode_file):
    """Read barcode from given file and return its value."""
    img = cv2.imread(barcode_file)
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        return barcodeData
