"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
"""
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


import timeit
import cProfile
import sys

#вариант через цикл

def sum_(n):
    el = 1
    sum_ = 0
    for i in range(n):
        sum_ += el
        el = el / 2 * (-1)
        i = i + 1
    return (sum_)

# print(sum_(2))
# print(timeit.timeit('sum_(2)', number=10000, globals=globals())) #0.005420100000000001
# print(timeit.timeit('sum_(4)', number=10000, globals=globals())) #0.011896200000000003
# print(timeit.timeit('sum_(8)', number=10000, globals=globals())) #0.018675499999999998
# print(timeit.timeit('sum_(16)', number=10000, globals=globals())) #0.030867099999999995


# cProfile.run('sum_(9999)')
#          4 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.001    0.001 lesson_4_task_1.py:10(sum_)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sum_(99999)')
   #
   #  4 function calls in 0.038 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.038    0.038    0.038    0.038 lesson_4_task_1.py:15(sum_)
   #      1    0.000    0.000    0.038    0.038 <string>:1(<module>)
   #      1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sum_(999999)')
# 4 function calls in 0.182 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.182    0.182    0.182    0.182 lesson_4_task_1.py:10(sum_)
#         1    0.000    0.000    0.182    0.182 <string>:1(<module>)
#         1    0.000    0.000    0.182    0.182 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




#вариант через рекурсию
sys.setrecursionlimit(2000)

def sum_2(n):
    if n == 1:
        return n
    elif n > 1:
        return 1 + sum_2(n - 1) / 2 * (-1)
#
# print(sum_2(5))
# print(timeit.timeit('sum_2(2)', number=10000, globals=globals())) #0.002916000000000002
# print(timeit.timeit('sum_2(4)', number=10000, globals=globals())) #0.008254900000000003
# print(timeit.timeit('sum_2(8)', number=10000, globals=globals())) #0.015494300000000003
# print(timeit.timeit('sum_2(16)', number=10000, globals=globals())) #0.03943970000000001

# cProfile.run('sum_2(999)')
   #       1002 function calls (4 primitive calls) in 0.001 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #  999/1    0.001    0.000    0.001    0.001 lesson_4_task_1.py:65(sum_2)
   #      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   #      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('sum_2(9999)')
   #       1496 function calls (4 primitive calls) in 0.002 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   # 1493/1    0.002    0.000    0.002    0.002 lesson_4_task_1.py:65(sum_2)
   #      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
   #      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# и здесь уже превышена глубина рекурсии RecursionError: maximum recursion depth exceeded in comparison




# вариант с геометрической прогрессией
def sum_3(n):
    return 1 * (1 - (-0.5) ** n) / (1 - (-0.5))

# print(sum_3(5))
# print(timeit.timeit('sum_3(2)', number=10000, globals=globals())) #0.003432099999999997
# print(timeit.timeit('sum_3(4)', number=10000, globals=globals())) #0.003318999999999999
# print(timeit.timeit('sum_3(8)', number=10000, globals=globals())) #0.0033190999999999984
# print(timeit.timeit('sum_3(16)', number=10000, globals=globals())) #0.0033170000000000005

# cProfile.run('sum_3(999)')
# cProfile.run('sum_3(9999)')
# cProfile.run('sum_3(99999)')
# cProfile.run('sum_3(99999999)')

# одинаковый вывод при всех n, поэтому вставляю один раз
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:102(sum_3)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод
# Первый вариант с циклом - линейная зависимость(n, t). Второй вариант с рекурсией - эксплуатируем стек вызова функции.
# В третьем варианте константная сложность, t не зависит от n.