# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

comands = argv[1]

with open(comands, 'r') as file:
    for file_lines in file:
        if file_lines.find('!') == -1 and file_lines.find(ignore[0]) == -1 and file_lines.find(ignore[1]) == -1 and file_lines.find(ignore[2]) == -1:
            print(file_lines.strip('\n'))