# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

import random
N = random.randint(1, 10)

sequence = []
for i in range(1, N + 1):
    item = (1 + 1*i)*i
    sequence.append(item)


print(f'Для N = {N} последовательность (1+1n)n примет вид: {sequence}.\nСумма чисел в последовательности = {sum(sequence)}.')