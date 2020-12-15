"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

"""

import random

SIZE = 6
MIN_ITEM = 0
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

max_item = array_1[0]
min_item = array_1[0]

max_i = 0
min_i = 0
sum_ = 0

for i, item in enumerate(array_1):
    if item > max_item:
        max_item = item
        max_i = i
    if item < min_item:
        min_item = item
        min_i = i

if min_i > max_i:
    min_i, max_i = max_i, min_i

for i in range(min_i + 1, max_i):
    sum_ += array_1[i]

print(sum_)


