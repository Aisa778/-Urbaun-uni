
def custom_write(file_name, strings):

    one_1 = open(file_name, 'a', encoding = 'UTF-8')

    ch_1=0
    strings_positions={}
    for i in strings:
        bb_2 = []
        ch_1 += 1
        b_1= one_1.tell()
        bb_2.append(ch_1)
        bb_2.append(b_1)
        a = tuple(bb_2)
        one_1.write(i+'\n')

        strings_positions[a] = i
    one_1.close()

    print(strings_positions)

    pass

p_1 = custom_write('persons.txt', ('Иванова', 'Петрова','Сидорова'))

# print(p_1)