from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, content):
        pass


class PDFFile(FileHandler):
    def read(self):
        return "Reading data from PDF file."

    def write(self, content):
        return f"Writing '{content}' to PDF file."


class CSVFile(FileHandler):
    def read(self):
        return "Reading data from CSV file."

    def write(self, content):
        return f"Writing '{content}' to CSV file."


class ExcelFile(FileHandler):
    def read(self):
        return "Reading data from Excel file."

    def write(self, content):
        return f"Writing '{content}' to Excel file."


for file_handler in (PDFFile(), CSVFile(), ExcelFile()):
    print(file_handler.read())
    print(file_handler.write("Report data"))
