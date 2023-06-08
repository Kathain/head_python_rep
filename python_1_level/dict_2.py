d = {
    1: 'one',         # Key cannot be a list (because it's changing value)
    2: 'two',
    3: [1, 2, 3]
}

print(d[1])   # we take a value of the first key, result -> one

d[4] = 'four'    # if we want to add new key

person = {
    'name': 'Vasya'
    'surname': 'Petrov'
    'age': 25
}
print(person)