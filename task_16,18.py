# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве
#  A[1..N]. Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя 
# строка содержит число X

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
#  к заданному числу X. Пользователь в первой строке вводит натуральное число N
#  – количество элементов в массиве. В последующих  строках записаны N целых
# чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

n = int(input('Введите число: '))
rand_number = [random.randint(0, 100) for i in range(1, 10)]
print(rand_number)
temp = 0
closest_num = -1
for i in range(len(rand_number)):
    min_d = max(rand_number) - n
    if int(rand_number[i]) == n:
        temp += 1
for i in set(rand_number):
    if abs(i - n) < min_d:
        min_d = abs(i - n)
        closest_num = i
print(f' - {temp} раз встречается в заданном списке число {n},\n - максимально близкое число {closest_num} ')
