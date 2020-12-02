"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""
# https://drive.google.com/file/d/1f1QbgF9-6WkMxyUTgFlDPxAs4eSFuum9/view?usp=sharing

n = int(input("Введите любое натуральное число"))
left = 0
right = n * (n + 1) / 2
for i in range(1, n+1):
    left += i
if left == right:
    print("Доказано")
else:
    print("Не доказано")
