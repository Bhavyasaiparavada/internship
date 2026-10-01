from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class PDFFile(FileHandler):
    def read(self):
        return "Reading PDF file."

    def write(self):
        return "Writing PDF file."


class CSVFile(FileHandler):
    def read(self):
        return "Reading CSV file."

    def write(self):
        return "Writing CSV file."


class ExcelFile(FileHandler):
    def read(self):
        return "Reading Excel file."

    def write(self):
        return "Writing Excel file."


for file_handler in [PDFFile(), CSVFile(), ExcelFile()]:
    print(file_handler.read(), file_handler.write())