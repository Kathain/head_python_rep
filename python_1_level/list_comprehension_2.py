import random

a = input().split()  # тут мы вводим 2 3 4 (но они получается имеют значение str)
a = [int(i) for i in a]  # тут мы преобразовываем str в int
print(a)

n = 5
m = 4

a = [[0] * m for i in range(n)]  # этим примером в итоге построили двухмерную матрицу
for i in a:
    print(i)

# так же можно использовать вложенные циклы

a = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(a)  # result - [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]


a = [(i * j) for i in 'abc' for j in [1, 2, 3] if i*j > 10]
print(a)