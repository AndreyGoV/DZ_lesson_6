'''
Задача №111335. Статистика по файлу

Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
Выведите три найденных числа в формате, приведенном в примере.

Для экономии памяти читайте файл посимвольно,
то есть не сохраняя целиком в памяти файл или отдельные его строки.
'''

print('Input file contains:')
lettes = 0
words = 0
lines = 0
with open('text.txt', 'r') as f:
    for i in f.read():
        if i.isalpha():
            lettes += 1
        if i == ' ' or i == '\n':
            words += 1
        if i == '\n':
            lines += 1

print(f'{lettes} letters')
print(f'{words + 1} words')
print(f'{lines} lines')
