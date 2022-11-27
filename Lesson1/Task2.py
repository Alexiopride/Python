# Напишите программу, которая на вход принимает 5 чисел
#  и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

counter = 0
number = int(input("Введите число "))
max_num = number
while counter < 4:
    number = int(input("Введите число "))
    if number > max_num:
        max_num = number
    counter += 1
print(max_num)


#Говно которое не работает
# sp = list()
# for i in range(5):
#     n = int(input())
#     sp.append(n)
# print(max(sp))
