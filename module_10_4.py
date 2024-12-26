import queue
from queue import Queue
import threading
import random
import time

from args import args


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
#
#
#

    def guest_arrival(self, *guests):
        for guest in guests:
            is_sit = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()
                    is_sit = True
                    break
        if not is_sit:
            print(f'{guest.name} в очереди')
            self.queue.put(guest)


    def discuss_guests(self):
        while not self.queue.empty() or any(
                table.guest and table.guest.is_alive() for table in self.tables
        ):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


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






