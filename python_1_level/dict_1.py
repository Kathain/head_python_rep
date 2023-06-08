# for creating a dict, use -> { key:value }
# e.g:   d = { key:value }

d = {             # the first way to create a dict
    'ukraine': 1,
    'germany': 2,
    'korea': 3
}
print(d)

r = dict(ukraine=1, germany=2, korea=3)    # the second way to create a dict.
print(r)                                  # #This way we use only for str format.

n = [['ukraine', 1], ['germany', 2], ['korea', 3]]   # the third way to create a dict
t = dict(n)
print(t)

q = dict.fromkeys(['a','b','c'])    # dict has a method fromkeys , result -> {'a': None, 'b': None, 'c': None}
print(q)                            # method fromkeys turns our values into keys.


w = dict.fromkeys(['a','b','c'], 100)    # every key will have a value 100. a:100, b:100 ...
print(w)

v = {}    # created an empty dict
p = dict()  # created an empty dict (way 2)

