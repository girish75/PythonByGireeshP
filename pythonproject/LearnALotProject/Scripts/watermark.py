import PyPDF2

with open(".SourceFolder\IGNITE.pdf",'rb') as inputfile:
    reader = PyPDF2.PdfFileReader(inputfile)

with open(".SourceFolder\wtr.pdf",'rb') as watermark:
    water_read = PyPDF2.PdfFileReader(watermark)

output_file = PyPDF2.PdfFileWriter()

# reader.getPage() returns page object and not number of pages.
for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    page.mergePage(water_read.getPage(0))
    output_file.addPage(page)

with open('watermarkedIGNITE.pdf','wb') as file:
    output_file.write(file)
	