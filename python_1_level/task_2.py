class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    # ниже идет Метод экземпляра
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # другой Метод экземпляра
    def speak(self, sound):
        return f"{self.name} says {sound}"


if __name__ == '__main__':
    Bill = Dog('Bill', 5, 'blue')
    print(Bill)