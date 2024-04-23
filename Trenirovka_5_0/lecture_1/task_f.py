# F. Миша и математика
# Миша сидел на занятиях математики в Высшей школе экономики и решал следующую задачу: дано n целых чисел
# и нужно расставить между ними знаки + и × так, чтобы результат полученного арифметического выражения
# был нечётным (например, между числами 5, 7, 2, можно расставить арифметические знаки следующим образом:
# 5×7+2=37). Так как примеры становились все больше и больше, а Миша срочно убегает в гости, от вас
# требуется написать программу решающую данную задачу.
# Формат ввода
# В первой строке содержится единственное число n (2≤n≤105). Во второй строке содержится n целых чисел
# ai, разделённых пробелами (−109≤ai≤109). Гарантируется, что решение существует.
# Формат вывода
# В одной строке выведите n−1 символ + или ×, в результате применения которых получается нечётный
# результат. (Для вывода используйте соответственно знаки «+» (ASCII код—43) и «x» (ASCII код—120),
# без кавычек).
# Пример 1
# Ввод	  Вывод
# 3       x+
# 5 7 2
# Пример 2
# Ввод	  Вывод
# 2       +
# 4 -5


n = int(input())
nums = (int(x) for x in input().split())
odds = [0] * n
for index, num in enumerate(nums):
    odds[index] = num % 2

sum_odds = sum(odds)
if sum_odds % 2:
    print('+' * (n - 1))
else:
    signs = []
    for i in range(1, n):
        if odds[i - 1] == 1:
            signs.append('x')
            print(''.join(signs) + '+' * (n - i - 1))
            break
        else:
            signs.append('+')
