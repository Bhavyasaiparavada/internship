from abc import ABC, abstractmethod


class FileProcessor(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, content):
        pass


class TextFile(FileProcessor):
    def read(self):
        print("Reading text file")

    def write(self, content):
        print("Writing to text file:", content)


class PDFFile(FileProcessor):
    def read(self):
        print("Reading PDF file")

    def write(self, content):
        print("Writing to PDF file:", content)


text_file = TextFile()
pdf_file = PDFFile()
text_file.read()
text_file.write("Hello")
pdf_file.read()
pdf_file.write("Hello")