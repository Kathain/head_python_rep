a = 1000
while a <= 2000:
    print(a)
    a = a + 1

a = 6785
while a != 190:
    print(a)
    a = a - 5


a, b = map(int, input().split())
count = 0
while a <= b:
    a = a * 3
    b = b * 2
    count = count + 1
print(count)


numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
while 4 in numbers:
    numbers.remove(4)
print(*numbers)


a = input()
while len(a) > 0:
    print(a)
    a = a[1:-1]


a = int(input())
count = 1
b = 2
while count ** 2 <= a:
    print(count ** 2)
    count = count + 1


a , b = map(int, input().split())
day = 1
while a < b:
    res1 = a * (15 / 100)
    a = a + res1
    day = day + 1
print(day)