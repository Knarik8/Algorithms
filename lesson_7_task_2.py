"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array_1 = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]
print(array_1)


def unite(m, n):
    c = []
    i = j = 0
    while i < len(m) and j < len(n):
        if m[i] < n[j]:
            c.append(m[i])
            i += 1
        else:
            c.append(n[j])
            j += 1
    if i < len(m):
        c += m[i:]
    if j < len(n):
        c += n[j:]
    return c

def merge(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge(array[: middle])
    right = merge(array[middle:])
    return unite(left, right)

print(merge(array_1))
