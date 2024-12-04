
def is_prime(sum_tree):

    def wrapper(*args):
        func_one = sum_tree(*args)

        z=0
        for j in range(2,func_one):

            if func_one % j==0:
                z+=1
            else:
                j+=1

        if z == 0:
            print ('простое число')
        else:
            print('не простое число')

        return func_one
    return wrapper


@is_prime
def sum_tree(*args):
    sum_1 = 0
    for i in args:
        sum_1+=i
    return sum_1




a = sum_tree(2,3,6)
print(a)


