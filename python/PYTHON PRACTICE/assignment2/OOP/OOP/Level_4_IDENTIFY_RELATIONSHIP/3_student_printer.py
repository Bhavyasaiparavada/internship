class Printer:
    def print_text(self, text):
        print(text)


class Student:
    def print_name(self, printer):
        printer.print_text("Asha")


print("USES-A: Student uses a Printer")
Student().print_name(Printer())
