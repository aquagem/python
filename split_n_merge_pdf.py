import os
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger


class PdfFunctions:
    def __init__(self, file, folderpath):
        self.file = file
        self.folderpath = folderpath

    def split_pdf(self):
        file = self.file
        inputpdf = PdfFileReader(open(file, 'rb'))
        for page in range(inputpdf.numPages):
            outpdf = PdfFileWriter()
            outpdf.addPage(inputpdf.getPage(page))
            with open("C:\\Users\\gauth\\Desktop\\tempc\\temp1\\DRUZ0001_{}.pdf".format(page), "wb") as outputStream:
                # with open("C:\\Users\\gauth\\Desktop\\temp\\temp1\\MARO0001_{}.pdf".format(page), "wb") as outputStream:
                outpdf.write(outputStream)

    def merge_pdf(self):
        folderpath = self.folderpath
        merger = PdfFileMerger()
        for file1 in os.listdir(folderpath):
            inputpdf = PdfFileReader(open(folderpath + file1, 'rb'))
            print(file1)
            print(inputpdf.numPages)
            merger.append(PdfFileReader(open(folderpath + file1, 'rb')))
        merger.write(folderpath + "/DRUZ0001.pdf")
        # merger.write(folderpath + "/MARO0001.pdf")


def main():
    pdf1 = PdfFunctions("C:\\Users\\gauth\\Desktop\\tempc\\DRUZ0001.pdf", "C:\\Users\\gauth\\Desktop\\tempc\\temp1\\")
    # pdf1 = PdfFunctions("C:\\Users\\gauth\\Desktop\\tempc\\MARO0001.pdf", "C:\\Users\\gauth\\Desktop\\tempc\\temp1\\")
    # pdf1.split_pdf()
    pdf1.merge_pdf()


if __name__ == "__main__":
    main()

