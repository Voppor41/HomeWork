from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)

    return print(f"Завершилась запись в файл {file_name}")


start_time = datetime.now()

thr_first = Thread(target=write_words, args=(10, 'example1.txt'))
thr_second = Thread(target=write_words, args=(30, 'example2.txt'))
thr_third = Thread(target=write_words, args=(200, 'example3.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example4.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
time_res = time_end - start_time
print(time_res)

start_time2 = datetime.now()

thr_fifth = Thread(target=write_words, args=(10, 'example5.txt'))
thr_sixth = Thread(target=write_words, args=(30, 'example6.txt'))
thr_seventh = Thread(target=write_words, args=(200, 'example7.txt'))
thr_eighth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_fifth.start()
thr_sixth.start()
thr_seventh.start()
thr_eighth.start()

thr_fifth.join()
thr_sixth.join()
thr_seventh.join()
thr_eighth.join()

time_end2 = datetime.now()
time_res2 = time_end2 - start_time2
print(time_res2)


