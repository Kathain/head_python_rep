# создание кортежа
a = (1, 2, 3, 4, 5)  # вариант создания кортежа 1 , если нужно пустой, то c = () or d = tuple()
b = 1, 2, 3, 4, 5  # вариант создания кортежа 2
c = tuple(range(5))  # вариант создания кортежа с одноименной функцией в котороую передаем итерабельную
# последовательность
d = tuple([1, 2, 3, 4])  # tuple + список
n = tuple((1, 2, 3, 4))  # tuple + сам кортеж
f = 1, # тут создали кортеж с одним элементом
print(n)


my_tuple = (1,2,3,29)
print(min(my_tuple),max(my_tuple))

a1 = (1,)*3
b1 = ('R',)*5
c1 = ('A',)*8
d1 = (2,)*5
result = a1 + b1 + c1 + d1
print(result)