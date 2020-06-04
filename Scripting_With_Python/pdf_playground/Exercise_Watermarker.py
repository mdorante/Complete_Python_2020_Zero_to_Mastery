import PyPDF2
import sys

input_pdf = sys.argv[1]
watermark_pdf = sys.argv[2]
output = sys.argv[3]

# A function that takes 3 params: the pdf that you want to watermark, the pdf containing the watermark
# and the name for the new watermarked pdf


def pdf_watermarker(pdf_in, pdf_water, out):
    pdf_obj = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    water_obj = PyPDF2.PdfFileReader(pdf_water)
    watermark_page = water_obj.getPage(0)

    for page in range(pdf_obj.getNumPages()):
        pdf_page = pdf_obj.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)

    with open(f'{output}', 'wb') as new_file:
        pdf_writer.write(new_file)


pdf_watermarker(input_pdf, watermark_pdf, output)
