from threading import Thread
import random
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name_guest):
        self.name_guest = name_guest
        super().__init__()

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            flag = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name_guest} сел(-а) за стол номер {table.number}')
                    flag = True
                    break
            if not flag:
                self.queue.put(guest)
                print(f'{guest.name_guest} в очереди')

    def discuss_guests(self):
        while True:
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name_guest} покушал и ушёл')
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f'{next_guest.name_guest} вышел из очереди '
                              f'и сел за стол номер {table.number}')

            if all(table.guest is None for table in self.tables) and self.queue.empty():
                print(f'Стол номер {table.number} свободен')
                break



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()