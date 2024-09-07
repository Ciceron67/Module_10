import threading
from threading import Thread, Lock
import random
import time


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()
        self.transaction = 100

    def deposit(self):
        for i in range(self.transaction):
            deposit = random.randint(50, 500)
            self.balance += deposit
            print(f'Пополнение: {deposit}. Баланс: {self.balance}')
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        time.sleep(0.001)

    def take(self):
        for i in range(self.transaction):
            deposit = random.randint(50, 500)
            print(f'Запрос на {deposit}')
            if deposit <= self.balance:
                self.balance -= deposit
                print(f'Снятие: {deposit}. Баланс: {self.balance}')
            if deposit > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
