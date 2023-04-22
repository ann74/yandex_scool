# Для транспортирования материалов из цеха А в цех В используется конвейер. Материалы упаковываются в одинаковые
# контейнеры и размещаются на ленте один за одним в порядке изготовления в цехе А. Каждый контейнер имеет степень срочности
# обработки в цехе В. Для упорядочивания контейнеров по степени срочности используют накопитель, который находится в
# конце конвейера перед входом в цех В. Накопитель работает пошагово, на каждом шаге возможны следующие действия:
# накопитель перемещает первый контейнер из ленты в цех В;
# накопитель перемещает первый контейнер из строки в склад (в складе каждый следующий контейнер помещается на предыдущий);
# накопитель перемещает верхний контейнер из склада в цех В.
# Напишите программу, которая по последовательности контейнеров определит, можно ли упорядочить их по степени срочности
# пользуясь описанным накопителем.
# Формат ввода
# Входной файл в первой строке содержит количество тестов N. Далее следует N строк, каждый из которых описывает отдельный
# тест и содержит целое число K (1 ≤ K ≤ 10000) — количество контейнеров в последовательности и K действительных чисел —
# степеней срочности контейнеров в порядке их поступления из цеха А (меньшим числам соответствует большая степень срочности).
# Формат вывода
# Каждая строка выходного файла должна содержать ответ для одного теста. Необходимо вывести 1, если необходимое
# упорядочивание возможно, или 0 в противном случае.
# Пример
# Ввод	        Вывод
# 2               1
# 2 2.9 2.1       0
# 3 5.6 9.0 2.0



for _ in range(int(input())):
    k, *conts = [float(x) for x in input().split()]
    k = int(k)
    stack = []
    temp = float('-inf')
    for cont in conts:
        while stack and stack[-1] < cont:
            temp = stack.pop()
        if cont < temp:
            print('0')
            break
        stack.append(cont)
    else:
        print('1')
