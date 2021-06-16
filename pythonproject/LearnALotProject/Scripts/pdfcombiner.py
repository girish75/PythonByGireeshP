import PyPDF2
# import sys

def pdf_combiner(pdflist):
    mergepdf = PyPDF2.PdfFileMerger()

    for pdf in pdflist:
        print(pdf)
        mergepdf.append(PyPDF2.PdfFileReader(pdf, 'rb'))
        mergepdf.write('super.pdf')
        print(mergepdf)


# inputpdflist = sys.argv[1:]
inputpdflist = ("IGNITE.pdf","dummy.pdf")
print(inputpdflist)
pdf_combiner(inputpdflist)
