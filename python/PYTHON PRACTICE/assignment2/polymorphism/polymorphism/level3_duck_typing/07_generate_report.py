class ExcelReport:
    def generate(self):
        print("Excel report generated")


class PDFReport:
    def generate(self):
        print("PDF report generated")


def generate_report(report):
    report.generate()


generate_report(ExcelReport())
generate_report(PDFReport())