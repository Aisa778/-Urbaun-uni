# from module_9_2 import second_result

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x)-len(y) for x, y in zip(first,second) if len(x)!=len(y))

second_result = (len(first[x])==len(second[y]) for x in range(len(first)) for y in range(len(second)) if x==y)


print(list(first_result))
print(list(second_result))
