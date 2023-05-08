a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print('FizzBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(a)


a,b,c = int(input()),int(input()),int(input())
if a == b and a == c:
    print(3)
elif a == b and a != c:
    print(2)
elif a == c and a != b:
    print(2)
elif b == c:
    print(2)
else:
    print(0)


a = int(input())
if a == 1:
    print('Январь')
elif a == 2:
    print('Февраль')
elif a == 3:
    print('Март')
elif a == 4:
    print('Апрель')
elif a == 5:
    print('Май')
elif a == 6:
    print('Июнь')
elif a == 7:
    print('Июль')
elif a == 8:
    print('Август')
elif a == 9:
    print('Сентябрь')
elif a == 10:
    print('Октябрь')
elif a == 11:
    print('Ноябрь')
elif a == 12:
    print('Декабрь')



a = int(input())
if a >= 65:
    print('Пожилой человек')
elif a <= 2:
    print('Младенец')
elif a >= 2 and a < 4:
    print('Малыш')
elif a >= 4 and a < 12:
    print('Ребенок')
elif a >= 12 and a < 19:
    print('Подросток')
elif a >= 19 and a <= 65:
    print('Взрослый человек')

a, b = len(input()), len(input())
if a < 7:
    print('Short')
elif a != b:
    print('Difference')
else:
    print('OK')
