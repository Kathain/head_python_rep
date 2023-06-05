from string import ascii_uppercase

zeroes = [0 for i in range(0,100)]
print(zeroes)

n = int(input())
a = [i for i in range(1,n+1)]
print(a)

print(4%2)

n = int(input())
с = 1
b = [i for i in range(с, n+1) if n % i == 0]
print(b)


n1 = int(input())
s = [i for i in range(n1, n1 ** 2 + 1) if i % 2 == 1]
print(s)


a, b = map(int, input().split())
print([i**2 for i in range(a, b+1)] if a <= b else [i**3 for i in range(a, b-1, -1)])

text = list(ascii_uppercase)
n = int(input())
m = [text[i] for i in range(0, n)]
print(m)

st = 'Create a list of the first letters of every word in this string'.split()
print([i[0] for i in st])




