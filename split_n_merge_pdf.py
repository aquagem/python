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
            with open("<pdf_filePath with filename>".format(page), "wb") as outputStream:
                outpdf.write(outputStream)

    def merge_pdf(self):
        folderpath = self.folderpath
        merger = PdfFileMerger()
        for file1 in os.listdir(folderpath):
            inputpdf = PdfFileReader(open(folderpath + file1, 'rb'))
            print(file1)
            print(inputpdf.numPages)
            merger.append(PdfFileReader(open(folderpath + file1, 'rb')))
        merger.write(folderpath + "/<filename>.pdf")


def main():
    pdf1 = PdfFunctions("<pdf_filePath with filename>", "<location where the files will be placed>")
    # pdf1.split_pdf()
    pdf1.merge_pdf()


if __name__ == "__main__":
    main()

