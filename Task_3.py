# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

# https://drive.google.com/file/d/1Ernd6ZkEZLZbVIV0kr8cp1B-SsGi5XoI/view?usp=sharing

x1 = float(input("Введите координаты первой точки, x1: "))
y1 = float(input("Введите координаты первой точки, y1: "))
x2 = float(input("Введите координаты второй точки, x2: "))
y2 = float(input("Введите координаты второй точки, y2: "))
if x1 == x2:
    print("Решений нет")
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2

    print("y = %.2f*x + %.2f" % (k, b))
