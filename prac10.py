# Name : PRATHAM MODI
# ID : 20CE056
# Aim :  Generate PDF file of your 3rd Semester Mark-sheet
# GITHUB LINK : https://github.com/prathammodi333/python-programs
from fpdf import FPDF
from PIL import Image

# pdf=PDF(orientation='L') # landscape
# pdf=PDF(unit='mm') #unit of measurement
# pdf=PDF(format='A4') #page format
pdf = FPDF('L', 'mm', 'A4')

# adding page
pdf.add_page()


marksheet = Image.open(r'D:\mt\python programs\python3.7program\practical10\IMG_20220320_203133_1.jpg')
ms = marksheet.convert('RGB')
ms.save(r'D:\mt\python programs\python3.7program\practical10\20ce056.pdf')