import PyPDF2

with open('..\..\Resources\pdf\IGNITE_Platform_User_Guide.pdf','rb') as file:
    print(file)
    readtext= PyPDF2.PdfFileReader(file)
    print(readtext.numPages)
    page= readtext.getPage(0) #this return page object
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('title.pdf', 'wb') as new_file:
        writer.write(new_file)
