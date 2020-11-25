# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

#https://drive.google.com/file/d/1Ernd6ZkEZLZbVIV0kr8cp1B-SsGi5XoI/view?usp=sharing

a = int(input("Введите трехзначное число"))
print(f"сумма: {a // 100 + a % 100 // 10 + a % 10}")
print(f"произведение: {(a // 100) * (a % 100 // 10) * (a % 10)}")
