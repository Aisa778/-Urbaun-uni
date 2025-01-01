# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt


# Pandas
# def read_f(name_file):
#     list_1=[]
#     # list_2=[]
#     with open (name_file, 'r') as f:
#         while True:
#             k= f.readline()
#             if not k:
#                 break
#
#             else:
#                list_1.append(k)
#
#     panda_1= pd.Series(list_1, index=['A','B','C','D','E','F'])
#
#     print(panda_1)
#
#     print(f'Максимальное значение = {max(panda_1)}')
#
#
# func=read_f(f'./file 1.txt')
# print(func)

# NumPy
# mas_1 = np.array([9.70,4.0,11.30,4.0,3.5,29.60,26.50,6.80,8.5,8.0,18.75,6.8,21.50,1.29,5.76,4.12])
# mas_2= np.array([10.25,4.21,11.30,3.99,3.50,29.54,26.0,8.67,4.23,3.95,15.10,4.78,2.57,1.30,6.5,4.17])
#
# diff= mas_1-mas_2
# # print(*diff)
# np.set_printoptions(precision=2, suppress=True)
# print (diff)

# визуализация на matplotlob

x_1 = list(range(0,16))
y_1 = [9.70,4.0,11.30,4.0,3.5,29.60,26.50,6.80,8.5,8.0,18.75,6.8,21.50,1.29,5.76,4.12]
x_2 = list(range(0,16))
y_2 = [10.25,4.21,11.30,3.99,3.50,29.54,26.0,8.67,4.23,3.95,15.10,4.78,2.57,1.30,6.5,4.17]
plt.plot(x_1,y_1,x_2,y_2)
# plt.plot(x_2,y_2)
plt.show()

