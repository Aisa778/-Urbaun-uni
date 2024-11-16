def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result+=i
        except TypeError:
            if type(i) != int:
                incorrect_data+=1
            # i+=1
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        culc_1 = len(numbers)  # количество значений в коллекции
        summ_1 = personal_sum(numbers)
        value_1 = summ_1[0] # сумма чисел коллекции
        value_2 = summ_1[1] # количество значений в коллекции, не являющихся int
        diff_culc = culc_1 - value_2  # количество чисел
        try:
            summ_av = value_1/ diff_culc
            print(f'среднее арифметическое значение:{summ_av}')
        except ZeroDivisionError:
            if diff_culc==0:
                print(f'данные для вычислений отсутствуют, значение:{culc_1}')

    except TypeError:
        print('В numbers записан некорректный тип данных')
# g=personal_sum(('l','k','o'))
# print(g)

# print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать