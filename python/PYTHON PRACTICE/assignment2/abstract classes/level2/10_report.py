from abc import ABC, abstractmethod


class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self):
        pass


class PDFReport(Report):
    def generate(self):
        return "PDF report generated."

    def export(self):
        return "PDF report exported."


class ExcelReport(Report):
    def generate(self):
        return "Excel report generated."

    def export(self):
        return "Excel report exported."


for report in [PDFReport(), ExcelReport()]:
    print(report.generate(), report.export())