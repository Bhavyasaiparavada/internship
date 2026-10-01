class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __gt__(self, other):
        return self.celsius > other.celsius


today = Temperature(30)
yesterday = Temperature(27)
print(today > yesterday)