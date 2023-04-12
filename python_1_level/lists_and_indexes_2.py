a = list(map(int, input().split()))
print(a[1])

a = list(map(int, input().split()))
print(a[2:5])


a = list(map(int, input().split()))
print(a[-3::])


a = list(map(int, input().split()))
print(a[1::3])


a = list(map(int, input().split()))
print(a[::-1])


top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top[-1] = 'Сверхъестественное'
top[2] = 'Настоящий детектив'
print(top)
