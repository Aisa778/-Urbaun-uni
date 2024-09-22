def cript_code():
    list_random = []  # создали пустой список для выходных значений
    # a = 0
    num_1 = 0
    # for i in range(3, 21):
    import random
    num_1 = random.randint(3, 20)
    list_random.append(num_1)
    list_random.append('-')
    numbers_1 = list(range(1, num_1))  
    numbers_2 = list(range(2, num_1))
    for i in numbers_1:
        for j in numbers_2:
            if j not in list_random:
                d = i + j
                if num_1 % d == 0 and j != i:
                    list_random.append(i)
                    list_random.append(j)

                else:
                    j += 1

    return list_random
crip = cript_code()
print(*crip)
