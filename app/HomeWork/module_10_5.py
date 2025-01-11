import time
from multiprocessing import Pool


# Функция для чтения данных из файла
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


# Основная часть программы
if __name__ == '__main__':
    # Список файлов для чтения
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # Линейный вызов функции read_info для каждого файла
    start_time = time.time()
    for filename in filenames:
        data = read_info(filename)
    print("Время выполнения линейного вызова:", time.time() - start_time)

    # Многопроцессорный вызов функции read_info для каждого файла
    start_time = time.time()
    with Pool() as pool:
        result = pool.map(read_info, filenames)

    print("Время выполнения многопроцессорного вызова:", time.time() - start_time)
