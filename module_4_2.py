# import math
list_1=[]
list_2=[]
def test_function(k):
    for i in a:
        list_1.append(i**2)

    def inner_function(k):
        for i in list_1:
            if i % 2 == 0:
                list_2.append('четное число')
            else:
                list_2.append('нечетное число')

                c="Я в области видимости функции test_function"
                print(c)
        #

        #
        return list_2

    # list_1=m
    inner_function(k)
    return list_1
a=(12,5,6)
# inner_function(a)

test_function(a)
print(list_1)
print(list_2)

