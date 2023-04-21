# На вокзале есть K тупиков, куда прибывают электрички. Этот вокзал является их конечной станцией, поэтому электрички,
# прибыв, некоторое время стоят на вокзале, а потом отправляются в новый рейс (в ту сторону, откуда прибыли).
# Дано расписание движения электричек, в котором для каждой электрички указано время ее прибытия, а также
# время отправления в следующий рейс. Электрички в расписании упорядочены по времени прибытия. Поскольку
# вокзал — конечная станция, то электричка может стоять на нем довольно долго, в частности, электричка,
# которая прибывает раньше другой, отправляться обратно может значительно позднее.
# Тупики пронумерованы числами от 1 до K. Когда электричка прибывает, ее ставят в свободный тупик с
# минимальным номером. При этом если электричка из какого-то тупика отправилась в момент времени X,
# то электричку, которая прибывает в момент времени X, в этот тупик ставить нельзя, а электричку,
# прибывающую в момент X+1 — можно.
# Напишите программу, которая по данному расписанию для каждой электрички определит номер тупика,
# куда прибудет эта электричка.
# Формат ввода
# Сначала вводятся число K — количество тупиков и число N — количество электропоездов
# (1 ≤ K≤100000, 1 ≤ N ≤ 100000). Далее следуют N строк, в каждой из которых записано по 2 числа:
# время прибытия и время отправления электрички. Время задается натуральным числом, не превышающим 109.
# Никакие две электрички не прибывают в одно и то же время, но при этом несколько электричек могут
# отправляться в одно и то же время. Также возможно, что какая-нибудь электричка (или даже несколько)
# отправляются в момент прибытия какой-нибудь другой электрички. Время отправления каждой электрички
# строго больше времени ее прибытия.
# Все электрички упорядочены по времени прибытия. Считается, что в нулевой момент времени все тупики на
# вокзале свободны.
# Формат вывода
# Выведите N чисел — по одному для каждой электрички: номер тупика, куда прибудет соответствующая электричка.
# Если тупиков не достаточно для того, чтобы организовать движение электричек согласно расписанию,
# выведите два числа: первое должно равняться 0 (нулю), а второе содержать номер первой из электричек,
# которая не сможет прибыть на вокзал.


def arrival(heap_list, x):  # Используем добавление элемента в кучу минимумов
    heap_list.append(x)
    pos = len(heap_list) - 1
    pos_parent = (pos - 1) // 2
    while pos > 0 and heap_list[pos] < heap_list[pos_parent]:
        heap_list[pos], heap_list[pos_parent] = \
            heap_list[pos_parent], heap_list[pos]
        pos = pos_parent
        pos_parent = (pos - 1) // 2


def departure(heap_list):  # Используем извлечение минимума из кучи минимумов
    if not heap_list:
        return 0
    ans = heap_list[0]
    heap_list[0] = heap_list[-1]
    pos = 0
    while pos*2 + 2 < len(heap_list):  # т.е. пока есть 2-е детей
        min_son_index = pos*2 + 1
        if heap_list[pos*2 + 2] < heap_list[pos*2 + 1]:
            min_son_index = pos*2 + 2
        if heap_list[pos] > heap_list[min_son_index]:
            heap_list[pos], heap_list[min_son_index] = \
              heap_list[min_son_index], heap_list[pos]
            pos = min_son_index
        else:
            break
    heap_list.pop()
    return ans


k, n = map(int, input().split())
tupics = [x for x in range(1, k + 1)]  # Куча минимумов
answer = []
trains = []
for i in range(n):
    train = input().split()
    trains.append((int(train[0]), -1, i))
    trains.append((int(train[1]), 1, i))
trains.sort()
for event in trains:
    if event[1] == -1:
        tupic = departure(tupics)
        if tupic == 0:
            print(0, len(answer) + 1)
            break
        else:
            answer.append(tupic)
    elif event[1] == 1:
        arrival(tupics, answer[event[2]])
else:
    print(*answer, sep='\n')
