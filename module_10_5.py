import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        file.readline()
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
    start = time.time()
    for file_name in filenames:
        read_info(file_name)
    print(time.time() - start)
# Многопроцессорный
    start = time.time()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    print(time.time() - start)
