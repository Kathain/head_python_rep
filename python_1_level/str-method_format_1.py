name = input()
surname = input()
text = '''Hello, {surname} {name}!'''.format(name=name, surname=surname)
print(text)
