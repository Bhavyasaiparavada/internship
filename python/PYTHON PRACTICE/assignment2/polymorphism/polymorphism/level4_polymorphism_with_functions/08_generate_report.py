class SalesReport:
    def generate(self):
        print("Sales report generated")


class StudentReport:
    def generate(self):
        print("Student report generated")


def generate_report(report):
    report.generate()


generate_report(SalesReport())
generate_report(StudentReport())