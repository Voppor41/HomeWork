from threading import Thread

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали')
        days = 1
        enemies = 100
        while enemies != 0:
            enemies -= self.power
            if enemies == 0:
                break
            print(f'{self.name} сражается {days} дней(дня), осталось {enemies} воинов.')
            days += 1

        return print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились')
