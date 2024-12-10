import threading
import time
from itertools import count


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        aliens = 100
        count = 0
        print (f'{self.name} на нас напали!')
        days = 100//self.power
        for i in range(days):
            count +=1
            aliens -= self.power
            time.sleep(1.0)
            print (f' {self.name} сражается {count} дней..., осталось {aliens}> воинов.')

        return print (f' {self.name} одержал победу спустя {count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
