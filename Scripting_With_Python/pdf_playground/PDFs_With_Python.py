import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader)  # <PyPDF2.pdf.PdfFileReader object at 0x7f1e83d6cd30>
    print(reader.numPages)  # 1
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('rotated_dummy.pdf', 'wb') as new_file:
        writer.write(new_file)


# NOTE: The open mode is rb which stands for Read Binary, because pypdf needs a binary file to work with
# same goes for wb

# Here, we read a pdf file, rotated one of it's pages (had only one page but doesn't matter) and saved the
# rotated version to a new file
