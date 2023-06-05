# [выражение for val in коллекция]
# в генираторах списков можно использовать условные констр. как например ниже
# [выражение for val in коллекция if условие]
import random
a = [0 for i in range(3)]
print(a)

a = [i for i in range(10)]
print(a)

a = [i**2 for i in range(10)]
print(a)

a = [i%4 for i in range(1, 15)]
print(a)

b = [i for i in 'hello']
print(b)

b = [i*5 for i in 'hello']
print(b)

# можно использовать различные функции ( например ord которая находит номер символа в таблице)

b = [ord(i) for i in 'hello']
print(b)

c = [random.randint(-10, 10) for i in range(10)]   # тут функция рандом, которая выводит рандомные числа в указанном нам диапазоне
print(c)

d = [abs(elem) for elem in c]      # тут функция которая отбрасывает минус у чисел
print(d)

a = [i * 2 for i in a]
print(a)

n = [random.randint(0,10) for i in range(10) if i%2 == 0]
print('tut n',n)

