"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
 Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
"""

import random
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)


def bubble(n):
    temp = 1
    while temp < len(array_1):
        for i in range(len(array_1)-1):
            if array_1[i] < array_1[i+1]:
                array_1[i], array_1[i+1] = array_1[i+1], array_1[i]
        temp += 1
    return array_1

print(bubble(array_1))