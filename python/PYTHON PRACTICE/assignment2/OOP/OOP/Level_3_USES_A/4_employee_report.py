class ReportGenerator:
    def generate(self, employee_name):
        print("Report for", employee_name)


class Employee:
    def __init__(self, name):
        self.name = name

    def create_report(self, generator):
        generator.generate(self.name)


Employee("Ravi").create_report(ReportGenerator())
