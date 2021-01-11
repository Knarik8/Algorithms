"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
from collections import deque
num_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
num_dict_2 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

result = deque()
a = deque(input("Введите первое шестнадцатеричное число "))
b = deque(input("Введите второе шестнадцатеричное число "))

if len(a) > len(b):
    diff = len(a) - len(b)
    for i in range(diff):
        b.appendleft(0)

if len(b) > len(a):
    diff = len(b) - len(a)
    for i in range(diff):
        a.appendleft(0)


print(a)
print(b)

temp = 0

for i in range(len(a)):
    last_a = a.pop()
    last_b = b.pop()
    if last_a in num_dict:
        last_a = num_dict.get(last_a)
    if last_b in num_dict:
        last_b = num_dict.get(last_b)
    sum_ = int(last_a) + int(last_b) + temp


    if sum_ > 15:
        temp += 1
        sum_ = sum_ - 16

        if sum_ in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result.appendleft(sum_)

        if sum_ in [10, 11, 12, 13, 14, 15]:
            sum_ = num_dict_2.get(sum_)
            result.appendleft(sum_)


    elif sum_ in [10, 11, 12, 13, 14, 15]:
        temp = 0
        sum_ = num_dict_2.get(sum_)
        result.appendleft(sum_)
    else:
        temp = 0
        result.appendleft(sum_)

print(f"Сумма чисел: {result}")
