import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.warriors = 100

    def run(self):
        print(f'{self.name} на нас напали!!!')
        while self.warriors > 0:
            time.sleep(1)
            self.days += 1
            self.warriors -= self.power
            if self.warriors < 0:
                self.warriors = 0
            print(f'{self.name}сражается {self.days},осталось {self.warriors} воинов.')

        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print(f'Битва закончилась!!!')
