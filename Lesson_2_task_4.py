"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

# https://drive.google.com/file/d/1f1QbgF9-6WkMxyUTgFlDPxAs4eSFuum9/view?usp=sharing

E = 1
sum = 0
n = int(input("Введите количество элементов"))
for i in range(n):
    sum += E
    E = E / 2 * (-1)
    i = i + 1
print(sum)
