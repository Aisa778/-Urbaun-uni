import threading
import time
from datetime import datetime
from time import sleep, localtime


def write_words(word_count, file_name):

    with open(file_name, 'w', encoding= 'utf-8') as file:
        for i in range(1,word_count+1):

            time.sleep(0.1)
            file.write(f"Какое-то слово № {i}\n")




    return print(f'Завершилась запись в файл {file_name}')
start =  time.time()
s = write_words(10, 'example1.txt')
s = write_words(20, 'example2.txt')
s = write_words(200, 'example3.txt')
s = write_words(100, 'example4.txt')
finish = time.time()
print(f'работа потоков {finish-start}')


start_1 =  time.time()
thread_1= threading.Thread(target=write_words, args=(10, 'example5.txt'))


thread_2= threading.Thread(target=write_words, args = (20,'example6.txt'))
# thread_2.start()
# thread_2.join()
#
thread_3= threading.Thread(target=write_words, args=(200,'example7.txt'))
# thread_3.start()
# thread_3.join()
#
thread_4= threading.Thread(target = write_words, args= (100,'example8.txt'))


thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

finish_1 = time.time()
print(f'работа потоков {finish_1-start_1}')
