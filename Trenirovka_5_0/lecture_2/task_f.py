# F. Колесо Фортуны
# Развлекательный телеканал транслирует шоу «Колесо Фортуны». В процессе игры участники шоу крутят большое колесо,
# разделенное на сектора. В каждом секторе этого колеса записано число. После того как колесо останавливается,
# специальная стрелка указывает на один из секторов. Число в этом секторе определяет выигрыш игрока.
# Юный участник шоу заметил, что колесо в процессе вращения замедляется из-за того, что стрелка задевает за
# выступы на колесе, находящиеся между секторами. Если колесо вращается с угловой скоростью v градусов в секунду,
# и стрелка, переходя из сектора X к следующему сектору, задевает за очередной выступ, то текущая угловая скорость
# движения колеса уменьшается на k градусов в секунду. При этом если v ≤ k, то колесо не может преодолеть
# препятствие и останавливается. Стрелка в этом случае будет указывать на сектор X.
# Юный участник шоу собирается вращать колесо. Зная порядок секторов на колесе, он хочет заставить колесо вращаться
# с такой начальной скоростью, чтобы после остановки колеса стрелка указала на как можно большее число. Колесо
# можно вращать в любом направлении и придавать ему начальную угловую скорость от a до b градусов в секунду.
# Требуется написать программу, которая по заданному расположению чисел в секторах, минимальной и максимальной
# начальной угловой скорости вращения колеса и величине замедления колеса при переходе через границу секторов
# вычисляет максимальный выигрыш.
# Формат ввода
# Первая строка входного файла содержит целое число n — количество секторов колеса (3 ≤ n ≤ 100).
# Вторая строка входного файла содержит n положительных целых чисел, каждое из которых не превышает 1000 —
# числа, записанные в секторах колеса. Числа приведены в порядке следования секторов по часовой стрелке.
# Изначально стрелка указывает на первое число.
# Третья строка содержит три целых числа: a, b и k (1 ≤ a ≤ b ≤ 109, 1 ≤ k ≤ 109).
# Формат вывода
# В выходном файле должно содержаться одно целое число — максимальный выигрыш.
# Пример 1
# Ввод	    Вывод
# 5           5
# 1 2 3 4 5
# 3 5 2


n = int(input())
nums = [(int(x), i) for (i, x) in enumerate(input().split())]
a, b, k = map(int, input().split())

nums.sort(reverse=True)
z = a // (n * k) - 1
flag_exit = False
for num in nums:
    speed_r = num[1] * k + 1 + z * n * k
    speed_l = (n - num[1]) * k + 1 + z * n * k
    while speed_r <= b or speed_l <= b:
        if a <= speed_r <= b or 0 <= (speed_r + k - 1 - a) < k:
            print(num[0])
            flag_exit = True
            break
        if a <= speed_l <= b or 0 <= (speed_l + k - 1 - a) < k:
            print(num[0])
            flag_exit = True
            break
        speed_r += n * k
        speed_l += n * k
    if flag_exit:
        break

