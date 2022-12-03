'''
Задача №111327. Числа могут быть где угодно

Во входном файле записано два целых числа, которые могут быть разделены
пробелами и концами строк. Выведите в выходной файл их сумму.

Указание. Считайте весь файл в строковую переменную при помощи
метода read() и разбейте ее на части при помощи метода split().
'''

with open('file_input.txt', 'r') as f_in:
    read_list = f_in.read().split()
    result = sum(map(int, read_list))
    print(result)

with open('file_output.txt', 'w') as f_out:
    f_out.write(f'{int(read_list[0])} + {int(read_list[1])} = {result}')
