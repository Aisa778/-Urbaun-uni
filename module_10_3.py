import threading
import random
import time


class Bank():
    # lock = threading.Lock
    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        # value = 0
        self.lock.acquire()
        for i in range(100):
            value = random.randint(50,500)
            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                i+=1
                time.sleep(0.001)

        pass


    def take(self):
        for i in range(100):
            value = random.randint(50,500)
            print (f'Запрос на {value}')
            if value <= self.balance:
                self.balance -= value
                print(f'Снятие: {value}. Баланс: {self.balance}')
            elif value>self.balance:
                print (f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            # el:se
            #     i+=1
        pass


bk = Bank(50,0)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')






