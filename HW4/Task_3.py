# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 


import os
os.system("cls")

import my_function as mf

    

numbers = mf.list_of_numbers()

numbers_list = mf.delete_repeat_numbers(numbers)
print(f"Из списка {numbers} были исключены повторяющиеся значения -> {numbers_list}")