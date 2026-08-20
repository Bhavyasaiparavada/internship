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


class HTMLReport(Report):
    def generate(self):
        return "HTML report generated."


reports = [PDFReport(), ExcelReport(), HTMLReport()]
for report in reports:
    print(report.generate())
