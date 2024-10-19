import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start = datetime.now()
        pool.map(read_info, filenames)
        end = datetime.now()
        result = end - start
        print(result)

'''for i in range(len(filenames)):
    start_time = datetime.now()
    read_info(filenames[i])
    end_time = datetime.now()
    result = end_time - start_time
    print(result)
'''
