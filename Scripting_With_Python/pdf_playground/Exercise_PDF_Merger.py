import PyPDF2
import sys

inputs = sys.argv[1:]

# A function that takes in multiple PDFs as parameters and combines them all into one big PDF


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')


pdf_combiner(inputs)
