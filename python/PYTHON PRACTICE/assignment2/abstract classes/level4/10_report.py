from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        return "PDF report generated."


class ExcelReport(Report):
    def generate(self):
        return "Excel report generated."


for report in [PDFReport(), ExcelReport()]:
    print(report.generate())