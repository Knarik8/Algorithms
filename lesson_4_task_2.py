"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""
import timeit
import cProfile

#первый вариант с помощью алгоритма «Решето Эратосфена»
# n - ищем до числа ...
# num - по счету простое число

def prime_num2(n, num):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b[num-1]
# print(timeit.timeit('prime_num2(1000, 5)', number=10000, globals=globals())) #5.0359226999999995
# print(timeit.timeit('prime_num2(1000, 50)', number=10000, globals=globals())) #5.2979513
# print(timeit.timeit('prime_num2(1000, 70)', number=10000, globals=globals())) #5.590287
# cProfile.run('prime_num2(1000, 5)')
 #
 # 172 function calls in 0.001 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
 #        1    0.001    0.001    0.001    0.001 lesson_4_task_2.py:18(prime_num2)
 #        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
 #      168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_num2(10000, 5)')
 # 1233 function calls in 0.010 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
 #        1    0.009    0.009    0.010    0.010 lesson_4_task_2.py:18(prime_num2)
 #        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
 #     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('prime_num2(100000, 5)')

 # 9596 function calls in 0.125 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.001    0.001    0.125    0.125 <string>:1(<module>)
 #        1    0.122    0.122    0.124    0.124 lesson_4_task_2.py:18(prime_num2)
 #        1    0.000    0.000    0.125    0.125 {built-in method builtins.exec}
 #     9592    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




#Второй — без использования «Решета Эратосфена»


def prime_num(n, num):
    lst=[]
    for i in range(2, n+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[num-1]


# print(timeit.timeit('prime_num(1000, 5)', number=10000, globals=globals())) #14.5421364
# print(timeit.timeit('prime_num(1000, 50)', number=10000, globals=globals())) #13.0060626
# print(timeit.timeit('prime_num(1000, 70)', number=10000, globals=globals())) #13.5270829

# cProfile.run('prime_num(1000, 5)')
# 172 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 lesson_4_task_2.py:88(prime_num)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_num(10000, 5)')

   # 1233 function calls in 0.112 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.112    0.112 <string>:1(<module>)
   #      1    0.112    0.112    0.112    0.112 lesson_4_task_2.py:88(prime_num)
   #      1    0.000    0.000    0.112    0.112 {built-in method builtins.exec}
   #   1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_num(100000, 5)')
 # 9596 function calls in 7.687 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    7.687    7.687 <string>:1(<module>)
 #        1    7.685    7.685    7.687    7.687 lesson_4_task_2.py:88(prime_num)
 #        1    0.000    0.000    7.687    7.687 {built-in method builtins.exec}
 #     9592    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# в варианте без использования «Решета Эратосфена» думала не дождусь уже timeit)
