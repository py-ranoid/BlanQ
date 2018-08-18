import PyPDF2

def removeSlashN(content):
    return content.replace('\n' , ' ')

def getPdfFileObject(pdf):
    pdfReader = None
    if(pdf == None):
        pdfFileObj = open('../PDFs/sample_1.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    else:
        pdfReader = PyPDF2.PdfFileReader(pdf)
    return pdfReader

def getCompletePdf(pdf):
    pdfReader = PyPDF2.PdfFileReader(pdf)
    numPages = pdfReader.numPages
    content = ''
    curPage = 1
    while curPage < numPages:
        content += removeSlashN(pdfReader.getPage(curPage).extractText())
    return content

def getPageContent(pageNumber , pdf):
    pdfReader = getPdfFileObject(pdf)
    content = pdfReader.getPage(pageNumber)
    text = removeSlashN(content.extractText())
    print(text)
    return text

