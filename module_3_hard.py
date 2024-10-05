data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
summ_all=0

def list_1(args):
    global summ_all
    data_1=args
    dict_1 = []
    dict_2 = []
    summ_dict = []
    for i in data_1:
        if isinstance(i, int):
            summ_all = summ_all + i
        elif isinstance(i, str):
            summ_all = summ_all+len(i)
        else:
            if isinstance(i, list):
               list_1(i)
            if isinstance(i, dict):
                summ_dict = [(key, value) for key, value in i.items()]
                list_1(summ_dict)
            if isinstance(i, set):
                list_1(i)

            if isinstance(i, tuple):
                tuple_1 = list(i)
                list_1(tuple_1)


            continue


# summ_all = 0
list_1(data_structure)

print(summ_all)