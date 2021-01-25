"""1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6"""

import hashlib

def substrings_count(string):
    substrings_h = []
    first = last = 0
    for _ in range(len(string)):
        for _ in range(len(string)):
            last += 1
            sub_ = string[first:last]
            sub_h = hashlib.sha1(sub_.encode('utf-8')).hexdigest()
            if sub_h not in substrings_h and sub_ != string and sub_ != '':
                substrings_h.append(sub_h)
        first = first + 1
        last = 0
    return len(substrings_h)

print(substrings_count("sova"))
print(substrings_count("papa"))