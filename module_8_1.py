def add_everything_up(a,b):

    try:

        x = a + b
        print(f'сложение выполнено, суммa равна:{x}')
    except TypeError:
        x=str(a)+str(b)

        print(f'сложение строк выполнено, сумма равна:, {x}')
        

add_everything_up('aa',2)
add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)