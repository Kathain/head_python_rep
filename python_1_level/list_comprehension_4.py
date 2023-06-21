colors = ['White', 'Blue', 'Yellow', 'Purple', 'Black', 'Green']
sizes = ['S', 'M', 'L', 'XL', 'XLL']
res = [(i,j) for i in colors for j in sizes]
print(res)


vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
a = [j for i in vector for j in i]
print(a)


