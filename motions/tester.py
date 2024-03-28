import easyocr 

reader = easyocr.Reader(['en'],gpu=False)
print(reader.readtext("image.png"))