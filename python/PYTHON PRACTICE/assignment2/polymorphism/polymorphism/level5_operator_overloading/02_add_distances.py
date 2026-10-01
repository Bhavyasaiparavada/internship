class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)


distance1 = Distance(5)
distance2 = Distance(8)
total = distance1 + distance2
print("Total distance:", total.meters, "meters")