#
a, b, *c = True, 8, 'hello', 999, 3,5,9
print(a,b,c) # результат будет True 8 ['hello', 999, 3, 5, 9] <- последний список это переменная c из за звездочки
*a,b,c = 'hello world'
print(a,b,c)  # result - ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r'] l d
*a,b,c = [2,3]
print(a,b,c)  # result - [] 2 3

''' 
! НО список не может состоять только из одного элемента 
никаких a,b,c = 2
'''

s = [4,10]
print(list(range(*s)))
'''
результатом будет - [4, 5, 6, 7, 8, 9], 
просто сделать print(list(range(s))) нельзя - будет ошибка

ЗВЕЗДОЧКА * распаковывает значение по переменным
'''

def f(*args):
    print(args)

f(1,2,3,4,5,6)
'''
при таком определении функции мы можем передавать
в нее любое количество обьектов
по итогу вывод будет в неизменяемом виде - кортеж
result - (1, 2, 3, 4, 5, 6)
'''

def f(*args):
    s = 0
    for i in args:
        s+=i
    return s
'''
тут все время будет считаться сумма, не зависимо от колличества введенных элементов
'''

# именнованные аргументы **kwargs

def n(**kwargs):
    print(kwargs)

n(a=1,b=4,c=9)

'''
будет возвращать словари
ключ и значение
{'a': 1, 'b': 4, 'c': 9}
'''

def b(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

b(a=100,b=200,c=300,g=400)

a, b, *c = range(5)
print(a,b,c)

