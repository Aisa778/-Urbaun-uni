

def min_func(args):
    list_1 = min(args)
    return list_1
    pass


def max_func(args):
    list_2 = max(args)
    return list_2
    pass

def len_func(args):
    list_3 = len(args)
    return list_3
    pass

def sum_func(args):
    sum_culc = 0
    for j in args:
        sum_culc+=j
    return sum_culc
    pass

def sorted_func(args):
    list_4 = sorted(args)
    return list_4
    pass

def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        result[i.__name__]= i(int_list)

    return result
    pass


print(apply_all_func([6, 20, 15, 9], max_func, min_func))

print(apply_all_func([6, 20, 15, 9], len_func, sum_func, sorted_func))
