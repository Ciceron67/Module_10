import time
from threading import Thread
from datetime import datetime

time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
    time.sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')



write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
res = end_time - time_start
print(f'Работа функции {res}')

thr1 = Thread(target=write_words(10, 'example5.txt'))
thr2 = Thread(target=write_words(30, 'example6.txt'))
thr3 = Thread(target=write_words(200, 'example7.txt'))
thr4 = Thread(target=write_words(100, 'example8.txt'))

time_start1 = datetime.now()
thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()
time_end1 = datetime.now()
res1 = time_end1 - time_start1
print(f'Работа потоков {res1}')
