a = input()
if a == 'Python':
    print('ДА')
else:
    print('НЕТ')


a = int(input())
if a >= 20000:
    a = a * 0.87
    print(a)
else:
    print(a)


a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)


a, b, c = map(int,input().split())
if a + b == c:
    print('YES')
else:
    print('NO')



a = list(map(int, input().split()))
if 3 in a:
    a.remove(3)

if 5 in a:
    a.remove(5)

if 7 in a:
    a.remove(7)

if 9 in a:
    a.remove(9)
print(a)



if (a := int(input())) > 10000:
        b = a - 10000
        print(f'Ого! {a}! Куда вам столько? Мы заберем {b}')
else:
    print(f'Сумма {a} не превышает лимит, проходите')


#if 'walrus' in (a:=str(input())):
if 'walrus' in (a:=(input())):
        print('Нашли моржа')
else:
    print('Никаких моржей тут нет')



if (a := (input()[::-1])) == (b := input()):
    print('YES')
else:
    print('NO')




if (a := str(input())) == (a[::-1]):
    print('YES')
else:
    print('NO')



a = int(input())
b = int(input())
c = int(input())
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('YES')
else:
    print('NO')