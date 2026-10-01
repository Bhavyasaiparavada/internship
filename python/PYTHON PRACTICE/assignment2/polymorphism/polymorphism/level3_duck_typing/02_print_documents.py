class Printer:
    def print(self):
        print("Printing a document")


class PDFPrinter:
    def print(self):
        print("Printing a PDF document")


def print_document(device):
    device.print()


print_document(Printer())
print_document(PDFPrinter())