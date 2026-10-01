class CPU:
    def process(self):
        print("CPU is processing")


class Computer:
    def __init__(self):
        self.cpu = CPU()


computer = Computer()
computer.cpu.process()
