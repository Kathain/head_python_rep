def outer() -> None:
    def say_hello() -> None:
        print('hello')

    def say_bye() -> None:
        print('bye')

    say_bye()
    say_hello()
outer()


def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition():
        print(x + y)

    def subtraction():
        print(x - y)

    def division():
        if y == 0:
            print('На ноль делить нельзя!')
        else:
            print(x / y)

    def multiplication():
        print(x * y)

    match
    operation:
    case
    'a': addition()
    case
    's': subtraction()
    case
    'd': division()
    case
    'm': multiplication()
    case
    _: print('Ошибка. Данной операции не существует')





