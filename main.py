from pdf2docx import Converter
my_path =( ".pdf")
output_path = ".docx"

cv = Converter(pdf_file=my_path)
cv. convert(docx_filename=output_path)
cv.close()
