numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
a = [111, 222, 789, 201]
numbers.extend(a)
print(numbers)

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.insert(5, 111)
numbers.insert(8, 222)
numbers.insert(0, 789)
numbers.insert(11, 201)
print(numbers)

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
numbers.extend(extra)
print(numbers)

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
a = numbers.pop()
b = numbers.pop(0)
c = numbers.pop(12)
d = numbers.pop(7)
print(numbers)
print(a+b+c+d)

numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
numbers.remove(3)
numbers.remove(5)
numbers.remove(7)
numbers.remove(9)

print(numbers)


numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.sort(reverse=True)
print(numbers)


a = list(map(int, input().split()))
a.reverse()
print(a)


a = list(map(int, input().split()))
print(a.count(999))

numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
copy_numbers = numbers.copy()
print(copy_numbers)

a = input().upper().split()
b1 = a[0]
b2 = a[1]
c1 = list(b1)
b1 = '-'.join(b1)
c2 = list(b2)
b2 = '-'.join(b2)
print(b1,b2)


a, b, c = map(str, input().split())
a1 = a[0]
b1 = b[0]
res = a1 + '.' + b1 + '.'
print(c,res)


a = input().split()
a = '\n'.join(a)
print(a)