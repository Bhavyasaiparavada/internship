from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self, filename):
        pass


class PDFReport(Report):
    def generate(self):
        return "PDF report generated."

    def export(self, filename):
        return f"Report exported as {filename}.pdf"


class ExcelReport(Report):
    def generate(self):
        return "Excel report generated."

    def export(self, filename):
        return f"Report exported as {filename}.xlsx"


for report in (PDFReport(), ExcelReport()):
    print(report.generate())
    print(report.export("monthly_report"))
