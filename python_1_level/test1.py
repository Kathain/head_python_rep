def check_password(n):
    n = list(n)
    numb = []
    up_let = []
    symbols = []
    flag = False
    for i in n:
        if i.isdigit():
            numb.append(i)
        elif i.isupper() == True:
            up_let.append(i)
        elif i in "!@#$%*":
            symbols.append(i)
    if len(numb) >= 3:
        if len(up_let) > 1:
            if len(symbols) > 1:
                if len(n) > 10:
                    print('Perfect password')





