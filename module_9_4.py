import random
from os import close
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
func_1 = list(map(lambda x, y: x==y, first, second))
print(func_1)

def get_advanced_writer(file_name):
    def write_everything(*data_base):
        
        print(type(data_base))
        with open(file_name, 'a') as d:
            for i in data_base:
                print(i)
                d.write(f'{i}\n')

    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__ (self):
        one_word = random.choice(self.words)

        return one_word



list_1 = ('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


z = get_advanced_writer('example.txt')
loc=(z(list_1))


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())