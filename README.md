# opticalCharacterRecognition
A simple Python project that extracts text from images using Tesseract OCR and saves the recognized text into a file. Useful for scanned documents, screenshots, and image-based text processing.

# Image Text Extraction using Python (pytesseract OCR)

This project demonstrates how to extract text from an image using **Tesseract OCR** with Python's **pytesseract** library.  
The extracted text is printed on the console and saved into a text file.



## 🚀 Features
- Extracts text from image files (JPG, PNG, etc.)
- Uses Tesseract OCR engine
- Saves extracted text to a file
- Simple and beginner-friendly Python code



## 🛠️ Technologies Used
- Python
- pytesseract
- PIL (Pillow)
- Tesseract OCR



## 📂 Project Structure
```
├── text1.jpg # Input image file
├── opticalCharacterRecognition.py # Python script
├── Newtxt # Output text file
└── README.md
```




## ⚙️ Installation & Setup

### 1️⃣ Install Tesseract OCR
Download and install Tesseract from:
https://github.com/tesseract-ocr/tesseract


Make sure the installation path is correct:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```


### 2️⃣ Install Required Python Libraries
```
pip install pytesseract 
```

### How to Run the Project

Place the image file (text1.jpg) in the project directory

### Run the Python script:
```
python opticalCharacterRecognition.py
```

### Extracted text will:

- Be displayed in the console

- Be saved in a file named Newtxt
