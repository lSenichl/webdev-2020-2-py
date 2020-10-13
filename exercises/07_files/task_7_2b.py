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
temp = 0

with open(comands, 'r') as file:
    for file_lines in file:
        for i in ignore:
            if file_lines.find(i) != -1:
                temp = temp + 1
            if temp == 0:
                print(file_lines.strip('\n'))
            temp = 0