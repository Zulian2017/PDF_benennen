import pdf2image
import os, sys
import poppler
try:
    from PIL import Image
except ImportError:
    pass
import pytesseract

PATH = '/home/kali/Documents/Test PDF/new'

i = 1

def delete_ppms():
    for file in os.listdir(PATH):
        if '.ppm' in file or '.DS_Store' in file:
            try:
                os.remove(PATH + file)
            except FileNotFoundError:
                pass

pdf_files = []

for f in os.listdir(PATH):
    full_name = os.path.join(PATH, f)
    #print(full_name)
    if os.path.isfile(full_name):
        name = os.path.basename(f)
        filename, ext = os.path.splitext(name)
        if ext == '.pdf':
            pdf_files.append(name)

for d in pdf_files:
    print(d)

