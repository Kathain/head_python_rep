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

people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]
phone_book = {i[1]:i[0] for i in people}
