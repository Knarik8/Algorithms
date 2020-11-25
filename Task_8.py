# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# https://drive.google.com/file/d/1Ernd6ZkEZLZbVIV0kr8cp1B-SsGi5XoI/view?usp=sharing
a = int(input("Введите год"))
if (a % 4 == 0 and a % 100 != 0) or (a % 4 == 0 and a % 100 == 0 and a % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")
