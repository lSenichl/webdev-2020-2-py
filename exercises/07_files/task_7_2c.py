# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

comands = argv[1]
argv_end_file = argv[2]
temp = 0

with open(comands, 'r') as file, open(argv_end_file, 'a') as end_file:
    for file_lines in file:
        for i in ignore:
            if file_lines.find(i) != -1:
                temp = temp + 1
            if temp == 0:
                end_file.write(file_lines)
            temp = 0