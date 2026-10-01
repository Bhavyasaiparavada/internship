class PDF:
    def open(self):
        print("Opening a PDF file")


class Word:
    def open(self):
        print("Opening a Word file")


class Excel:
    def open(self):
        print("Opening an Excel file")


pdf = PDF()
word = Word()
excel = Excel()
pdf.open()
word.open()
excel.open()