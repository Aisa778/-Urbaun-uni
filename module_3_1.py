calls = 0

def count_calls():
    global calls
    calls+=1

def string_info():
    # global calls
    str_1=input('Введите название любого города в России:')
    cort_1=len(str_1)
    cort_2=str_1.upper()
    cort_3 = str_1.lower()
    all_cort = (cort_1,cort_2,cort_3)
    print(all_cort)
    # calls+=1
    count_calls()
string_info()

def is_contains():
    # global calls
    # list_to_search=[]
    string = input('Введите день недели:').lower()
    a_1 = input('Какой сегодня день недели?').lower()
    a_2= input('Как вас зовут?')
    a_3= str(input('Cколько Вам лет?'))
    list_to_search=[a_1,a_2,a_3]
    if string in list_to_search:
        a_4='True'
    else:
        a_4='False'
    low_1=a_1.upper()
    print(a_1,low_1,a_2,a_3)
    print (a_4)
    count_calls()
    # calls+=1
is_contains()

print(calls)