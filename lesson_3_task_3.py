"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

for i, item in enumerate(array_1):
    if item > max_item:
        max_item = item
        max_i = i
    if item < min_item:
        min_item = item
        min_i = i
temp = array_1[max_i]
array_1[max_i] = array_1[min_i]
array_1[min_i] = temp

print(array_1)






# for i in range(SIZE-1):
#     if array_1[i+1] > max:
#         max = array_1[i+1]
#
# for i in range(SIZE-1):
#     if array_1[i+1] < min:
#         min = array_1[i+1]


