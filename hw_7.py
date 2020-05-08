# Прочтем папки и файлы из директории.
# https://pythoner.name/walk

import os

#tree = os.walk('folder')
#print(tree) # <generator object walk at 0x00C5D4C0>
# Генератор похож на список, но он не хранит данные в памяти.

# for files in tree:
#     print(files)

'''
('folder', ['subfolder1', 'subfolder2'], [])
('folder\\subfolder1', [], ['2.txt', '3.txt'])
('folder\\subfolder2', ['subfolder2_1'], ['1.txt'])
('folder\\subfolder2\\subfolder2_1', [], ['4.txt'])

Каждый кортеж возвращает 3 элемента:
1.Адрес очередного каталога в виде строки.
2.В форме списка имена подкаталогов первого уровня вложенности для данного каталога.
3.В виде списка имена файлов данного каталога.
'''

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root, dirs, files)
        level = root.count(os.sep)
        # print(root, files, level)
        indent = ' ' * 4 * level
        # print(root, files, level, indent)
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        # print(root, files, level, indent, subindent)
        for file in files:
            print(f'{sub_indent}{file}')



read_dir('folder')