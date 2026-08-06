# Дан файл с данными клиентов. Необходимо извлечь все почтовые адреса в отдельный список.
# Для решения задачи необходимо составить регулярное выражение и использовать модуль re.
#
# Примечание. Допустимые доменные зоны - .ru, .com
#
# Пример входных данных:
# Иван ivan228@mail.ru Алексей alexdarkstalker98@gmail.com Петр thegreat@yandex.ru Руслан cheremsha@yahoo.com
#
# Пример выходных данных:
# ivan228@mail.ru
# alexdarkstalker98@gmail.com
# thegreat@yandex.ru
# cheremsha@yahoo.com

from re import finditer
# data = "Иван ivan228@mail.ru Алексей alexdarkstalker98@gmail.com Петр thegreat@yandex.ru Руслан cheremsha@yahoo.com"
# pattern = r"\S+@[a-z]+\.(ru|com)"
#
# matches = [match.group() for match in finditer (pattern, data)]
# print(matches)

from re import finditer
from timeit import timeit

with open (r"task-email.txt", encoding ="utf-8") as file:
    data = file.readline()

pattern = r"\S+@[a-z]+\.(ru|com)"

matches = [match.group() for match in finditer (pattern, data)]
print(*matches, sep = "\n")# * распаковка

#1способ. Через цикл
for match in matches:
    print(match)

#2способ. Методы обработки строк
#print("\n".join(matches))


# def f1():
#     print(*matches, sep = "\n")
# def f2():
#     print("\n".join(matches))
# def f3():
#     for match in matches : print(match)



