try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def recText(filename):
    text=pytesseract.image_to_string(Image.open(filename))
    return text

info=recText("text1.jpg")
print(info)


#Save the info(text extracted) from img

file=open("Newtxt","a")
file.write(info)
file.close()
print("Written successfull")


