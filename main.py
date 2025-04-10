import pytesseract
from PIL import Image
from docx import Document
import os

class Converter:
    def __init__(self, image_to_convert):
        self.image_to_convert = image_to_convert
        
        
        
    def displayImage(self):
        image = Image.open(self.image_to_convert)
        print(self.image_to_convert)
        image.show()
        return image
        
    def convertImage(self):
        d_image = self.displayImage()
        extracted_text = pytesseract.image_to_string(d_image)
        text_paragraph = extracted_text.split('\n')
        print(extracted_text)
        return text_paragraph
        
    def save_to_word(self, output="output.docx"):
        document = Document()
        os.makedirs("UPLOADS", exist_ok=True)
        output_path = os.path.join('UPLOADS', output)
        for paragraph_txt in self.convertImage():
            document.add_paragraph(paragraph_txt)
            
        document.save(output_path)
        
        
        
    
#running my code here
