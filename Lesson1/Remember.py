
# # ОСновные типы данных:
# #integer
# #sroke
# #bool
# #float
# _____________________________________________
# a = 5
# b = 'abc'
# c = True
# d = 0.5
# print(type(a)) #integer
# print(type(b)) #sroke
# print(type(c)) #bool
# print(type(d)) #float
# ____________________________________________
# a = 0
# if a > 0:
#     print("Положительное")
# elif a == 0:
#     print("Число", a, "равно нулю")
# else:
#     print("Отрицательное")
# ______________________________________________
# Основные два цикла For и While.

# For - Если мы хотим повторить что то несколько раз и чаще всего мы знаем сколько раз.

# for i in range (5):
#     print("Mama")

# Тоже самое можно сделать циклом While, но его чаще используем когда мы не знаем сколько раз нужно повторить.

# i = 0
# while i < 5:
#     print("Mama")
#     i += 1
# _________________________________________________________
# # Целочисленное деление и еление с остатком:
# n = 567

# # Целочисленное:
# print(n // 10) #Получим 56

# # Деление с остатком:
# print(n % 10) #Получим 7 
# ___________________________________________________________

# Списки
# sp = list()
# sp = []
# sp.append(5)
# sp.append(8)
# print(sp)


#  Обращение к спискам
# sp = [1, 5, 3, 89, 3]
# print(sp[0])
# Укажет первый элемент под индексом 0

# print(sp[-1])
# Укажет последний элемент (обратная индексация)


# Можно перебирать список с помощью цикла For.
# Например по индексам:

# for i in range (0, len(sp)):    #(0, len(sp)) - от нуля до длинны списка.
    # print(sp[i])  #выводит в столбик
    # print(sp[i], end=" ")  #выводит в одну строчку

# Или по элементам:
# for el in sp:
    # print(el, end=" ") #выводит в одну строчку.

# Выведет весь список с скобками и запятыми:
# print(sp)

# # Выведет весь список без скобок:
# print(*sp)
