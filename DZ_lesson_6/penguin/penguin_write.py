'''Задача: Пингвины

Написать программу, которая записывает в файл количество
пингвинов по заданному числу n от 1 до 9.
'''

n = 3

str1 = '   _~_    '
str2 = '  (o o)   '
str3 = ' /  V  \\  '
str4 = '/(  _  )\\ '
str5 = '  ^^ ^^   '

lst = [str1, str2, str3, str4, str5]

with open('penguin.txt', 'w', encoding='utf-8') as f:
    for i in lst:
        f.write(f'{i * n}\n')

