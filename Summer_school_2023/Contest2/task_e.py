# Дан массив a из n чисел. Найдите минимальное количество чисел, после удаления которых попарная разность оставшихся
# чисел по модулю не будет превышать 1, то есть после удаления ни одно число не должно отличаться от какого-либо
# другого более чем на 1.
# Формат ввода
# Первая строка содержит одно целое число n (1≤n≤2⋅105) — количество элементов массива a. Вторая строка содержит n
# целых чисел a1,a2,…,an (0≤ai≤105) — элементы массива a.
# Формат вывода
# Выведите одно число — ответ на задачу.
# Пример 1
# Ввод	       Вывод
# 5              3
# 1 2 3 4 5
# Пример 2
# Ввод	               Вывод
# 10                     4
# 1 1 2 3 5 5 2 2 1 5

n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
max_length = 1
right = 1
for left in range(n - 1):
    while right < n and nums[right] - nums[left] <= 1:
        right += 1
    max_length = max(max_length, right - left)
print(n - max_length)