from datetime import datetime
from itertools import count
from queue import Queue
import time
import datetime
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
start_time = datetime.datetime.now()
for name in filenames:
    # start_time = datetime.datetime.now()
    f = read_info(name)
    
end_time = datetime.datetime.now()
elapsed_time = end_time-start_time
    # count.append(elapsed_time)
print(elapsed_time)

# if __name__ == '__main__':
#     start_time2 = datetime.datetime.now()
#     with Pool(4) as pool:
#         pool.map(read_info, filenames)
#
#     end2 = datetime.datetime.now()
#     time_of_multiprocessing = end2 - start_time2
#
#     print(time_of_multiprocessing)





