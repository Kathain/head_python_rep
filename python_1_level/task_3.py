class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

    def drive(self, number):
        self.number = number
        self.mileage = self.mileage + self.number


if __name__ == '__main__':
    bmw = Car('red', 25000)
    print(bmw)
    audi = Car('black', 0)
    audi.drive(100)
    print(audi)
