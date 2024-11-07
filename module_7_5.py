import os
from os import mkdir
import time

directory = '.'
f_1 = 'module_7_1.py'
print(os.getcwd())
print(os.walk(directory))
if os.path.exists(directory):
    os.chdir(directory)
else:
    os.mkdir(directory)


for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory)
        filetime = os.path.getmtime(f_1)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(f_1)
        parent_dir = os.path.dirname(f_1)

        


#
print(f'Обнаружен файл: {f_1}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
