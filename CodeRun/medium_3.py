# 3. Вывести маршрут максимальной стоимости
# В левом верхнем углу прямоугольной таблицы размером N×M находится черепашка. В каждой клетке таблицы записано
# некоторое число. Черепашка может перемещаться вправо или вниз, при этом маршрут черепашки заканчивается в
# правом нижнем углу таблицы.
# Подсчитаем сумму чисел, записанных в клетках, через которую проползла черепашка (включая начальную и конечную
# клетку). Найдите наибольшее возможное значение этой суммы и маршрут, на котором достигается эта сумма.
# Формат ввода
# В первой строке входных данных записаны два натуральных числа N и M, не превосходящих 100 — размеры таблицы.
# Далее идет N строк, каждая из которых содержит M чисел, разделенных пробелами — описание таблицы. Все числа
# в клетках таблицы целые и могут принимать значения от 0 до 100.
# Формат вывода
# Первая строка выходных данных содержит максимальную возможную сумму, вторая — маршрут, на котором достигается
# эта сумма. Маршрут выводится в виде последовательности, которая должна содержать N-1 букву D, означающую
# передвижение вниз и M-1 букву R, означающую передвижение направо. Если таких последовательностей несколько,
# необходимо вывести ровно одну (любую) из них.
# Пример 1
# Ввод          Вывод
# 5 5           74
# 9 9 9 9 9     D D R R R R D D
# 3 0 0 0 0
# 9 9 9 9 9
# 6 6 6 6 8
# 9 9 9 9 9


import sys


def main():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    table = []
    for _ in range(n):
        row = list(map(int, input().split()))
        table.append(row)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = table[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n][m])

    answer = []
    x = n
    y = m
    while x > 1 or y > 1:
        temp = dp[x][y] - table[x - 1][y - 1]
        if y > 1 and dp[x][y - 1] == temp:
            answer.append('R')
            y -= 1
        else:
            answer.append('D')
            x -= 1
    print(*answer[::-1])


if __name__ == '__main__':
    main()