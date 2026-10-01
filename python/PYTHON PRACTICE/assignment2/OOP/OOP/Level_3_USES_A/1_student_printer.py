class Printer:
    def print_text(self, text):
        print("Printing:", text)


class Student:
    def __init__(self, name):
        self.name = name

    def print_details(self, printer):
        printer.print_text("Student: " + self.name)


Student("Asha").print_details(Printer())
