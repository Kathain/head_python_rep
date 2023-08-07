class Dog:
    speacies = 'Canis familiaris'  # это атрибут класса (тк находится ВНЕ init.

    def __init__(self, name, age, breed):  # init метод - задает исходное состояние обьекта.Присвает значения свойствам обьекта
        self.name = name  # это атрибуты экземпляров класса
        self.age = age
        self.breed = breed

    def print_name(self):
        print(self.name)

    # ниже идет Метод экземпляра
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # другой Метод экземпляра
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class Bulldog(Dog):
    def speak(self, sound='Woowh'):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound = 'Bark'):
        return f"{self.name} says {sound}"





if __name__ == '__main__':
    buddy = Dog('Buddy', 9, 'Bulldog')
    print(buddy.speak('woow'))
    jimm = Bulldog('Jimm',3,'Bulldog')
    print(jimm.speak())






