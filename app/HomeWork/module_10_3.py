from threading import Thread, Lock
from random import randint
import time

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        transaction = 1
        for transaction in range(100):
            self.lock.acquire()
            money = int(randint(50, 500))
            self.balance += money
            print(f'Пополнение: {money}. Баланс {self.balance}')
            if self.balance >= 500:
                self.lock.release()
            else:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        transaction = 1
        for transaction in range(100):
            money = int(randint(50, 500))
            print(f"Запрос на {money}")
            self.lock.acquire()
            if money <= self.balance:
                self.balance -= money
                print(f'Снятие: {money}. Баланс {self.balance}')
                self.lock.release()
            else:
                print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)

    def run(self):
        self.deposit()
        self.take()


bk = Bank()

th1 = Thread(target=bk.deposit)
th2 = Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
