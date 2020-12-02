# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# https://drive.google.com/file/d/1Ernd6ZkEZLZbVIV0kr8cp1B-SsGi5XoI/view?usp=sharing
a = int(input("Введите три разных числа. Первое: "))
b = int(input("Второе: "))
c = int(input("Третье: "))
if (a > b and a < c) or (a < b and a > c):
    print(f"Среднее число: {a}")
elif (b > a and a < c) or (a > b and a > c and b > c):
    print(f"Среднее число: {b}")
else:
    print(f"Среднее число: {c}")
