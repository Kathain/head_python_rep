b = int(input())
b1 = str(b + 1)
b2 = str(b - 1)
text1 = '''For the number {b} the previous one will be the number {b2}.'''.format(b=b, b2=b2)
text2 = '''For the number {b} the following will be the number {b1}.'''.format(b=b, b1=b1)
print(text1)
print(text2)
