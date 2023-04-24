# Игра в пьяницу
# В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по
# одной верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, которые
# кладутся под низ его колоды. Тот, кто остается без карт – проигрывает. Для простоты будем
# считать, что все карты различны по номиналу, а также, что самая младшая карта побеждает
# самую старшую карту ("шестерка берет туза"). Игрок, который забирает себе карты, сначала
# кладет под низ своей колоды карту первого игрока, затем карту второго игрока (то есть карта
# второго игрока оказывается внизу колоды). Напишите программу, которая моделирует игру в
# пьяницу и определяет, кто выигрывает. В игре участвует 10 карт, имеющих значения от 0 до 9,
# большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.
# Формат ввода
# Программа получает на вход две строки: первая строка содержит 5 чисел, разделенных пробелами
# — номера карт первого игрока, вторая – аналогично 5 карт второго игрока. Карты перечислены
# сверху вниз, то есть каждая строка начинается с той карты, которая будет открыта первой.
# Формат вывода
# Программа должна определить, кто выигрывает при данной раздаче, и вывести слово first или
# second, после чего вывести количество ходов, сделанных до выигрыша. Если на протяжении 106
# ходов игра не заканчивается, программа должна вывести слово botva.
# Пример 1
# Ввод	     Вывод
# 1 3 5 7 9    second 5
# 2 4 6 8 0
# Пример 2
# Ввод	     Вывод
# 2 4 6 8 0    first 5
# 1 3 5 7 9
# Пример 3
# Ввод	     Вывод
# 1 7 3 9 4    second 23
# 5 8 0 2 6


from collections import deque

cards = [int(x) for x in input().split()]
first = deque(cards)
cards = [int(x) for x in input().split()]
second = deque(cards)

n = 0
while n <= 1000000 and (len(first) > 0 and len(second) > 0):
    temp = [first.popleft(), second.popleft()]
    if temp[0] == 0 and temp[1] == 9:
        first.extend(temp)
    elif temp[0] == 9 and temp[1] == 0:
        second.extend(temp)
    elif temp[0] > temp[1]:
        first.extend(temp)
    else:
        second.extend(temp)
    n += 1
if n == 1000000:
    print('botva')
elif len(first) == 0:
    print('second', n)
elif len(second) == 0:
    print('first', n)