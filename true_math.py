from math import inf


def divide(first, second):
    if second==0:
        print(inf)
    else:
        print(first/second)

first=int(input('введите первое число:'))
second=int(input('введите второе число:'))

divide(first,second)