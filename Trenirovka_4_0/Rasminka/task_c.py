# Путешествие по Москве.
# Мэрия Москвы основательно подготовилась к празднованию тысячелетия города в 2147 году, построив под столицей
# бесконечную асфальтированную площадку, чтобы заменить все существующие в городе автомобильные дороги.
# В память о кольцевых и радиальных дорогах разрешили двигаться по площадке только двумя способами:
# В сторону точки начала координат или от неё. При этом из точки начала координат разрешено двигаться в
# любом направлении.
# Вдоль окружности с центром в начале координат и радиусом, который равен текущему расстоянию до начала
# координат. Двигаться вдоль такой окружности разрешается в любом направлении (по или против часовой стрелки).
# Вам, как ведущему программисту ответственной инстанции поручено разработать модуль, который будет определять
# кратчайший путь из точки A, с координатами (xA, yA) в точку B с координатами (xB, yB). Считайте,
# что менять направление движения можно произвольное количество раз, но оно должно всегда соответствовать
# одному из двух описанных выше вариантов.
# Формат ввода
# В первой строке ввода заданы четыре целых числа xA, yA, xB и yB, по модулю не превосходящие 106.
# Формат вывода
# Выведите одно число — минимальное расстояние, которое придётся преодолеть по пути из точки A в точку B,
# если не нарушать правил дорожного движения. Ваш ответ будет принят, если его абсолютная или относительная
# погрешность не превосходит 10-6.
# Пример 1
# Ввод	                         Вывод
# 444444 333333 888888 666666      555555.000000000000
# Пример 2
# Ввод	                         Вывод
# -444444 -333333 888888 666666    1666665.000000000000
import math


def quoter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    elif x > 0 and y == 0:
        return 5
    elif x == 0 and y > 0:
        return 6
    elif x < 0 and y == 0:
        return 7
    return 8


def corner(tan_, quot) -> float:
    if quot == 5:
        return 0
    elif quot == 6:
        return math.pi / 2
    elif quot == 7:
        return math.pi
    elif quot == 8:
        return math.pi * 3 / 2
    elif quot == 1:
        return math.atan(tan_)
    elif quot == 2 or quot == 3:
        return math.pi + math.atan(tan_)
    else:
        return math.pi * 2 + math.atan(tan_)


x_A, y_A, x_B, y_B = map(int, input().split())
R_A = (x_A**2 + y_A**2) ** 0.5
R_B = (x_B**2 + y_B**2) ** 0.5
q_A = quoter(x_A, y_A)
q_B = quoter(x_B, y_B)
if q_A not in (6, 8):
    tan_A = y_A / x_A
else:
    tan_A = float('inf')
if q_B not in (6, 8):
    tan_B = y_B / x_B
else:
    tan_B = float('inf')
if tan_A == tan_B or abs(tan_A - tan_B) < 0.0000001:
    if q_A == q_B:
        res = abs(R_B - R_A)
    else:
        res = R_B + R_A
else:
    dist1 = R_B + R_A
    corner_A = corner(tan_A, q_A)
    corner_B = corner(tan_B, q_B)
    min_corner = min(abs(corner_B - corner_A), math.pi * 2 - abs(corner_B - corner_A))
    min_R = min(R_A, R_B)
    dist2 = min_R * min_corner + abs(R_B - R_A)
    res = min(dist2, dist1)

print(res)
