# H. Забег по стадиону
# Стадион представляет собой окружность длиной L метров, на которой отмечена точка старта.
# По стадиону бегают Кирилл и Антон. У каждого мальчика есть своя точка старта (она представляет
# собой расстояние в метрах от старта, отсчитанное по часовой стрелке) и своя скорость в метрах
# в секунду (положительная скорость означает, что мальчик бежит по часовой стрелке, отрицательная
# — что бежит против часовой, а нулевая — что он стоит на месте).
# Вам нужно сказать, через какое минимальное время мальчики окажутся на одинаковом расстоянии
# от точки старта. Обратите внимание, что в этот момент они могли находиться в разных точках.
# Формат ввода
# В единственной строке вводится 5 целых чисел L,x1,v1,x2,v2 (1≤L≤109, 0≤x1,x2<L, ∣∣v1∣∣,∣∣v2∣∣≤
# 109) — длины стадиона в метрах, начальная точка Кирилла, скорость Кирилла, начальная точка
# Антона, скорость Антона.
# Формат вывода
# В первой строке выведите слово «YES», если случится момент, когда мальчики будут на одинаковом
# расстоянии от старта, или «NO», если такого момента не произойдёт.
# Если ответ «YES», то во второй строке выведите одно вещественное число — через какое минимальное
# количество времени мальчики окажутся на одинаковом расстоянии от старта.
# Ваш ответ будет считаться правильным, если его абсолютная или относительная ошибка не
# превосходит 10−9.
# Пример 1
# Ввод	     Вывод
# 6 3 1 1 1    YES
#              1.0000000000
# Пример 2
# Ввод	       Вывод
# 12 8 10 5 20   YES
#                0.3000000000
# Пример 3
# Ввод	      Вывод
# 5 0 0 1 2     YES
#               2.0000000000
# Пример 4
# Ввод	       Вывод
# 10 7 -3 1 4    YES
#                0.8571428571


L, x1, v1, x2, v2 = map(int, input().split())
times = []
if abs(x1) > abs(x2):
    x1, x2 = x2, x1
    v1, v2 = v2, v1

if x1 == x2 or x1 == (L - x2):
    print('YES')
    print(0)
    quit()

if v1 != v2:
    t3 = (x2 - x1) / (v1 - v2)
    if t3 >= 0:
        times.append(t3)
    t4 = (x2 - x1 - L) / (v1 - v2)
    if t4 >= 0:
        times.append(t4)
if (v1 + v2) != 0:
    t5 = (L - x1 - x2) / (v1 + v2)
    if t5 >= 0:
        times.append(t5)
    t6 = (2 * L - x1 - x2) / (v1 + v2)
    if t6 >= 0:
        times.append(t6)
    t7 = ( -x1 - x2) / (v1 + v2)
    if t7 >= 0:
        times.append(t7)
    t8 = (-L - x1 - x2) / (v1 + v2)
    if t8 >= 0:
        times.append(t8)

if times:
    print('YES')
    print(min(times))
else:
    print('NO')

