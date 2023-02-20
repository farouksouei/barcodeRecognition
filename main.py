from fastapi import FastAPI
import BarcodeGeneration

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/generateExams/{class}")
async def say_hello(name: str):
    listOfNames = ['name1', 'name2', 'name3']
    for name in listOfNames:
        BarcodeGeneration.generate_barcode(name, 'barcode' + name + '.png')
    return {"message": f"Hello {name}"}


@app.get("/barcode/")
async def get_barcode(name: str):
    barcodeValue = BarcodeGeneration.read_barcode('barcode.png')
    return {"message": f"Barcode value is {barcodeValue}"}


@app.get("/generatePDF/{PDFname}")
async def generate_PDF(PDFname: str):
    return {"message": f"PDF name is {PDFname}"}
