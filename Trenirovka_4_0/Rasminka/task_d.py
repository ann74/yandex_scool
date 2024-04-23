# Анагарамма.
# Задано две строки, нужно проверить, является ли одна анаграммой другой. Анаграммой называется строка,
# полученная из другой перестановкой букв.
# Формат ввода
# Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.
# Формат вывода
# Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.
# Пример 1
# Ввод	  Вывод
# dusty     YES
# study
# Пример 2
# Ввод	  Вывод
# rat       NO
# bat

from collections import Counter

word1 = input()
word2 = input()
dict1 = Counter(word1)
dict2 = Counter(word2)
print(('NO', 'YES')[dict1 == dict2])