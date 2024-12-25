from itertools import count
from queue import Queue
import time
# import multiprocessing
from multiprocessing.pool import Pool



def read_info(name):
    all_data=[]
    # for i in name:
    with open (name, 'r') as file:
        # while True:
            line_1 = file.readline()
            all_data.append(line_1)
    return name
    # print()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# count=[]
# for name in filenames:
#     start_time = time.time()
#     f = read_info(name)
#     end_time = time.time()
#     elapsed_time = end_time-start_time
#     count.append(elapsed_time)
# print(count)

if __name__ == '__main__':
    count = []
    with Pool(1) as pool:
        start_time = time.time()
        result = pool.map(read_info, filenames)
        end_time = time.time()
        elapsed_time = end_time - start_time
        count.append(elapsed_time)
    print(count)




