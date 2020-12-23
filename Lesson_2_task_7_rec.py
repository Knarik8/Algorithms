"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
# https://drive.google.com/file/d/1f1QbgF9-6WkMxyUTgFlDPxAs4eSFuum9/view?usp=sharing


def left(n):
    if n == 1:
        return n
    elif n > 1:
        return n + left(n-1)

n = int(input("Введите любое натуральное число"))
right = n * (n + 1) / 2

while True:
    if left(n) == right:
        print("Доказано")
    elif left(n) != right:
        print("Не доказано")
    break
