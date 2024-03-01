# Не минимум на отрезке.
# Задана последовательность целых чисел a1, a2, …, an. Задаются запросы: сказать любой элемент последовательности
# на отрезке от L до R включительно, не равный минимуму на этом отрезке.
# Формат ввода
# В первой строке содержатся два целых числа N, 1 ≤ N ≤ 100 и M, 1 ≤ M ≤ 1000 — длина последовательности и
# количество запросов соответственно.
# Во второй строке — сама последовательность, 0 ≤ ai ≤ 1000.
# Начиная с третьей строки перечисляются M запросов, состоящих из границ отрезка L и R, где L, R - индексы массива,
# нумеруются с нуля.
# Формат вывода
# На каждый запрос выведите в отдельной строке ответ — любой элемент на [L, R], кроме минимального. В случае,
# если такого элемента нет, выведите "NOT FOUND".
# Пример 1
# Ввод	                  Вывод
# 10 5                      NOT FOUND
# 1 1 1 2 2 2 3 3 3 10      2
# 0 1                       NOT FOUND
# 0 3                       10
# 3 4                       3
# 7 9
# 3 7
# Пример 2
# Ввод	            Вывод
# 4 2                 NOT FOUND
# 1 1 1 2             2
# 0 2
# 0 3

n, m = map(int, input().split())
a = [int(x) for x in input().split()]
for i in range(m):
    l, r = map(int, input().split())
    for i in range(l + 1, r + 1):
        if a[i] > a[i - 1]:
            print(a[i])
            break
        if a[i] < a[i - 1]:
            print(a[i - 1])
            break
    else:
        print('NOT FOUND')
