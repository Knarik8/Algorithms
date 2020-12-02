"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
# https://drive.google.com/file/d/1f1QbgF9-6WkMxyUTgFlDPxAs4eSFuum9/view?usp=sharing

x = input("Введите натуральное число")
chet = 0
nechet = 0
for i in x:
    k = int(i)
    if k % 2 == 0:
        chet += 1
    elif k % 2 != 0:
        nechet += 1
print(f"Количество четных цифр: {chet}, нечетных: {nechet}")