from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass


class PDFFile(FileHandler):
    def read(self):
        return "Reading a PDF file."


class CSVFile(FileHandler):
    def read(self):
        return "Reading a CSV file."


for file_handler in [PDFFile(), CSVFile()]:
    print(file_handler.read())