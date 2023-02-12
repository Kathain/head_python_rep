import math
a,b,c = map(int, input().split())
res1 = (a + b) * 2
res2 = res1 * c
res3 = res2 / 16
print(math.ceil(res3))
