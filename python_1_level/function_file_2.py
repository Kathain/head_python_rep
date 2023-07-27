def count_args(*args):
    return len(args)


def check_sum(*args):
    res = 0
    for i in args:
        res += i
    if res >= 50:
        print('verification passed')
    else:
        print('not enough')



def multiply(*args:int):
    a = 1
    for i in args:
        a*=i
    return a


def only_one_positive(*args: int):
    spisok = []
    for i in args:
        if i > 0:
            spisok.append(i)
    if len(spisok) > 1 or len(spisok) == 0:
        return False
    else:
        return True

def print_goods(*args):
    count = 1
    for i in args:
        if type(i) == str and len(i) > 0:
            print(f"{count}. {i}")
            count+=1
        if count == 1:
            print("Нет товаров")


def info_kwargs(**kwargs):
    for a, b in sorted(kwargs.items()):
        print(a, b, sep=' = ')


def create_actor(**kwargs):
    f = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46
    }

    return f | kwargs













