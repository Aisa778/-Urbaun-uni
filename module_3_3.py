# Задача №1
# def print_params(*a = 1, b = 'строка', c = True):
#     print(a,b,c)
## print_params()
#
# def print_params(*args):
#     print(*args)
## print_params(1, 'строка',True)
#
# def print_params(*args):
#     print(*args)
## print_params()
#
# def print_params(a,b,c):
#     print(a,b,c)
## k = [1,2,3,4,5]
## print_params(k,1,3

# def print_params(a,b,c):
#     print(a,b,c)
## print_params(b=25)
# def print_params(*args):
#     print(*args)
# k = [1,2,3,4,5]
# print_params(*k)

# Задача №2
# def print_params(a,b,c):
#     print (a,b,c)
# values_list=[11,'Метод', True]
# values_dict={'a':'Среда', 'b':'Пятница', 'c':'Воскресенье'}
# # print_params(*values_list)
# print_params(**values_dict)

# Задача №3
def print_params(a,b,c):
    print (a,b,c)
values_list_2=[11,'Метод']
# print_params(*values_list_2, 42)
print_params(3,*values_list_2)