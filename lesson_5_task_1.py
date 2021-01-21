"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import deque

companies = {}
profitable_companies = deque()
unprofitable_companies = deque()

n = int(input("Введите количество предприятий"))
for i in range(1, n+1):
    company_name = input(f"Введите наименование {i}-го предприятия")
    company_profit = 0
    for j in range(1, 5):
        quarterly_profit = float(input(f"Введите прибыль за {j} квартал:"))
        company_profit += quarterly_profit
        companies[company_name] = company_profit

average_profit = round(sum(companies.values()) / n, 2)
for key in companies:
    if companies[key] > average_profit:
        profitable_companies.append(key)
    else:
        unprofitable_companies.append(key)

print(f"Средняя прибыль за год для всех предприятий: {average_profit}")
print(f"Компании с прибылью выше среднего: {profitable_companies}")
print(f"Компании с прибылью ниже среднего: {unprofitable_companies}")
