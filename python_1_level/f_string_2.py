a = int(input())
b = int(input())
res1 = f'{a} / {b} = {a/b}'
res2 = f'{a} // {b} = {a//b}'
res3 = f'{a} % {b} = {a%b}'
print(res1)
print(res2)
print(res3)


x = int(input())
y = int(input())
z = int(input())
text = f'''Vector A({x}, {y}, {z})
Vector B({x + 5}, {y + 5}, {z + 5})'''
print(text)


a1, b1 = float(input()), int(input())
text1 = f'''Current dollar rate is {a1}. You want to buy {b1} dollars
You must pay {a1 * b1}'''
print(text1)


m, k = int(input()), int(input())
print(f"point({m = }, {k = })")


number_pi = 3.141592653589793
print(f'{number_pi:.6f}')



w = float(input())
print(f'{w:.2f}')

w1 = int(input())
print(f'{w1:010d}')


p = int(input())
sep = '-'
print(f'{p:{sep}^15}')


text2 = input()
sep2 = '&'
print(f"|{text2:{sep2}^20}|")
print(f"|{text2:{sep2}>20}|")
print(f"|{text2:{sep2}<20}|")
