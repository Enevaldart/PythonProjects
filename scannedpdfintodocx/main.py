
import pytesseract
from PIL import Image
import io
import docx

# Load the scanned image into memory
img = Image.open('testerimg.png')

# Use Pytesseract to extract text from the image
text = pytesseract.image_to_string(img)

# Create a new Word document and write the text to it
doc = docx.Document()
doc.add_paragraph(text)
doc.save('scanned_image.docx')