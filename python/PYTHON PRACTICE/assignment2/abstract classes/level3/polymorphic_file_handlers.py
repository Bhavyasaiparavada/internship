from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass


class PDFFile(FileHandler):
    def read(self):
        return "Reading content from a PDF file."


class CSVFile(FileHandler):
    def read(self):
        return "Reading rows from a CSV file."


class ExcelFile(FileHandler):
    def read(self):
        return "Reading worksheets from an Excel file."


file_handlers = [PDFFile(), CSVFile(), ExcelFile()]
for file_handler in file_handlers:
    print(file_handler.read())
