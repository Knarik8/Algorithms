"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

# https://drive.google.com/file/d/1f1QbgF9-6WkMxyUTgFlDPxAs4eSFuum9/view?usp=sharing

n = int(input("Сколько чисел хотите ввести?"))
s = int(input("Какую цифру будем искать?"))
count = 0
for i in range(1, n + 1):
    a = int(input(f"введите число {str(i)}:"))
    while a > 0:
        if a % 10 == s:
            count += 1
        a = a // 10
print(f"Цифра {s} встречается {count} раз")
