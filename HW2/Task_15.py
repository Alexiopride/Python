# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_number(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод!")
            
N = get_number("Введите целое число: ")

result = []
factorial = 1
for i in range(1, N + 1):
    factorial = factorial * i
    result.append(factorial)

print(f'Для N = {N}: {result}')