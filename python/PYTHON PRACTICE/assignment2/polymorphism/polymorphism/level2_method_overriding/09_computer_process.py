class Computer:
    def process(self):
        print("Computer is processing data")


class Laptop(Computer):
    def process(self):
        print("Laptop processes personal tasks")


class Desktop(Computer):
    def process(self):
        print("Desktop processes office tasks")


class Server(Computer):
    def process(self):
        print("Server processes network requests")


laptop = Laptop()
desktop = Desktop()
server = Server()
laptop.process()
desktop.process()
server.process()