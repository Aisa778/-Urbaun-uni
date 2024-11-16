def add_everything_up(a,b):

    try:

        x = a + b
        print(f'сложение выполнено, суммa равна:{x}')
    except TypeError:
        if type(a) == str and type(b) == int:
            x = a + str(b)
            print(f'сложение строк выполнено, сумма равна:, {x}')
        elif type(a) == str and type(b) == float:
            x = a + str(b)
            print(f'сложение строк выполнено, сумма равна:, {x}')
        elif type(a) == int and type(b) == str:
            x = str(a) + b
            print(f'сложение строк выполнено, сумма равна:, {x}')
        elif type(a) == float and type(b) == str:
            x = str(a) + b
            print(f'сложение строк выполнено, сумма равна:, {x}')
            # print(f'сложение не выполнено')
        else:
            print('Сложение не может быть выполнено')

add_everything_up('aa',2)
add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)