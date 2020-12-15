"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""
import random

SIZE = 6
MIN_ITEM = -100
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

max_minus_item = MIN_ITEM

for i, item in enumerate(array_1):
    if item < 0 and item > max_minus_item:
        max_minus_item = item
        max_minus_i = i
print(f"Максимальный отрицательный элемент: {max_minus_item}, его индекс: {max_minus_i}")
