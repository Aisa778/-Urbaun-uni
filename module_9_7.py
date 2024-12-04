
def is_prime(sum_tree):

    def wrapper(*args):
        func_one = sum_tree(*args)
        if func_one > 1:
            z=0
            for j in range(2,func_one):

                if func_one % j==0:
                    z+=1
                else:
                    j+=1

            if z == 0:
                print ('простое число')
            else:
                print('составное число')
        elif func_one <= 1:
            print('число меньше или равное 1 не может быть простым')
        # elif func_one ==0:
        #     print('число 0 не является простым или составным')

        return func_one
    return wrapper


@is_prime
def sum_tree(*args):
    sum_1 = 0
    for i in args:
        sum_1+=i
    return sum_1




a = sum_tree(2,2,4)
print(a)


