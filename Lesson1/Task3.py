# Напишите программу, которая будет на вход принимать число N
#  и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

number_N = int(input("Введите число N -> "))
for i in range(-number_N, number_N + 1):
   print(i, end=" ")