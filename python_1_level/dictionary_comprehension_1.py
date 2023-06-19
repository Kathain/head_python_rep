# key:value

a = {word: len(word) for word in ['hello', 'hi', 'www']}
# result : {'hello': 5, 'hi': 2, 'www': 3}
print(a)

data = {
    'Джефф Безос': '177',
    'ИлоН МаСк': '126',
    'бернар АрнО': '150',
    'БиЛл ГеЙтС': '124',
}

new_data = {key.title():int(value) for key, value in data.items()}
# result - {'Джефф Безос': 177, 'Илон Маск': 126, 'Бернар Арно': 150, 'Билл Гейтс': 124}
print(new_data)


# without dictionary comprehension it looks like that

new_data = {}
for key, value in data.items():
    new_data[key.title()] = int(value)
print(new_data)

users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [3, 'username', '1234'],
    [51, 'qwerty', '1234']
]

new_users = {user[0]:user for user in users}
print(new_users)




