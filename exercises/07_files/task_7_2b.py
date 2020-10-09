# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

comands = argv[1]

with open(comands, 'r') as file, open('config_sw1_cleared.txt', 'a') as end_file:
    for file_lines in file:
        if file_lines.find(ignore[0]) == -1 and file_lines.find(ignore[1]) == -1 and file_lines.find(ignore[2]) == -1:
            end_file.write(file_lines)