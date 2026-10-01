from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        return "Report: " + self.title


class PDFReport(Report):
    def generate(self):
        return "PDF report generated."


report = PDFReport("Sales")
print(report.display_report_info())
print(report.generate())