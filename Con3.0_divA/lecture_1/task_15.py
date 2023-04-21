# Формат XML является распространенным способом обмена данными между различными программами. Недавно программист
# Иванов написал небольшую программу, которая сохраняет некоторую важную информацию в виде XML-строки.
# XML-строка состоит из открывающих и закрывающих тегов.
# Открывающий тег начинается с открывающей угловой скобки (<), за ней следует имя тега — непустая строка из строчных
# букв латинского алфавита, а затем закрывающая угловая скобка (>). Примеры открывающих тегов: <a>, <dog>.
# Закрывающий тег начинается с открывающей угловой скобки, за ней следует прямой слеш (/), затем имя тега — непустая
# строка из строчных букв латинского алфавита, а затем закрывающая угловая скобка. Примеры закрывающихся тегов:
# </a>, </dog>.
# XML-строка называется корректной, если она может быть получена по следующим правилам:
# • Пустая строка является корректной XML-строкой.
# • Если A и B — корректные XML-строки, то строка AB, получающаяся приписыванием строки B в конец строки A,
# также является корректной XML-строкой.
# • Если A — корректная XML-строка, то строка <X>A</X>, получающаяся приписыванием в начало A открывающегося тега,
# а в конец — закрывающегося с таким же именем, также является корректной XML-строкой. Здесь X — любая непустая
# строка из строчных букв латинского алфавита.
# Например, представленные ниже строки:
# <a></a>
# <a><ab></ab><c></c></a>
# <a></a><a></a><a></a>
# являются корректными XML-строками, а такие строки как:
# <a></b>
# <a><b>
# <a><b></a></b>
# не являются корректными XML-строками.
# Иванов отправил файл с сохраненной XML-строкой по электронной почте своему коллеге Петрову. Однако, к сожалению,
# файл повредился в процессе пересылки: ровно один символ в строке заменился на некоторый другой символ.
# Требуется написать программу, которая по строке, которую получил Петров, восстановит исходную XML-строку,
# которую отправлял Иванов.
# Формат ввода
# Входной файл содержит одну строку, которая заменой ровно одного символа может быть превращена в корректную XML
# -строку. Длина строки лежит в пределах от 7 до 1000, включительно. Строка содержит только строчные буквы
# латинского алфавита и символы «<» (ASCII код 60), «>»(ASCII код 62) и «/»(ASCII код 47). Строка во входном файле
# заканчивается переводом строки.
# Формат вывода
# Выходной файл должен содержать корректную XML-строку, которая может быть получена из строки во входном файле
# заменой ровно одного символа на другой. Если вариантов ответа несколько, можно вывести любой.


def check_seq(seq: list) -> bool:
    stack = []
    if seq[0] != '<' or seq[-1] != '>':
        return False
    seq1 = ''.join(seq[1:-1]).split('><')
    for tag in seq1:
        if tag.isalpha():
            stack.append(tag)
        elif tag[0] == '/':
            if stack and stack.pop() == tag[1:]:
                continue
            else:
                return False
        else:
            return False
    if stack:
        return False
    return True


s_start = list(input())
s = s_start.copy()
symbols = '<>/abcdefghijklmnopqrstuvwxwz'
flag = False
for i in range(len(s)):
    for j in symbols:
        s[i] = j
        if check_seq(s):
            flag = True
            break
    if flag:
        break
    else:
        s[i] = s_start[i]

print(''.join(s))
