a = input()
print(f'''Мое имя {a}!''')

name = str(input())
age = int(input())
text = f"""Hello {name.upper()}. You are {age} years old."""
print(text)

name1 = input()
year1 = int(input())
res = year1 + 77
text1 = f"""{name1}, вам исполнится 77 лет в {res}"""
print(text1)


a1 = int(input())
b1 = a1 // 60
c1 = a1 % 60
text2 = f'{a1} сек - это {b1} мин. {c1} сек.'
print(text2)


x, y = map(int, input().split())
res2 = x * y
text3 = f'''Разрешение экрана: {x} x {y}.
Общее количество пикселей = {res2}.'''
print(text3)




