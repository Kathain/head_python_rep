n = int(input())
database = {}
count = 0
for i in range(n):
    login = input()
    if login not in database:
        database[login] = 0
        print(f'OK')

    elif login in database:
        database[login] += 1
        database[f"{login}{database[login]}"] = 0
        print(f"{login}{database[login]}")




countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
for i range(len(countries)):
    if city in countries:
        print(city[i])


spisok = []
first_list = xhr["data"]["WhiteListEmployee"]
for i in first_list:
    if 'EmployeeTitle' in i:
        spisok.append(i['EmployeeTitle'])
        print(spisok)
