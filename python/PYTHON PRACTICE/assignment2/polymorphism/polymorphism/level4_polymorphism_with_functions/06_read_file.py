class TextFile:
    def read(self):
        print("Reading a text file")


class PDFFile:
    def read(self):
        print("Reading a PDF file")


def read_file(file):
    file.read()


read_file(TextFile())
read_file(PDFFile())