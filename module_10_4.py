import queue
from queue import Queue
import threading
import random
import time

from args import args


#
# import args
#
#
class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

    def is_free(self):
        if self.guest == None:
            message_1 = None
        else:
            message_1 = self.guest

        # return  message_1

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        pause_1 = random.randint(3,10)
        time.sleep(pause_1)

        pass

class Cafe:
    def __init__(self, queue, *tables):
        self.queue = Queue()
        self.tables = tables


    def guest_arrival(self, *guests):
        for i in guests:
            for j in self.tables:
                if j.guest is None:
                    j.guest = i
                    Guest.start(i)
                    print(f'{i.name} сел(-а) за стол номер {j.number}')
                    break

                else:
                    self.queue.put(i)

    def discuss_guests(self):
        if not self.queue.empty:# or 'None' in self.tables:
            for k in self.tables:
                if Guest.is_alive(self.name):
                    print(f'{Guest.name} покушал(-а) и ушёл(ушла)')
                    print (f'Стол номер {k.number} свободен')
                    k.guest = None

                    q = queue.get()
                    k.number = q




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# print(tables)

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']


guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()










