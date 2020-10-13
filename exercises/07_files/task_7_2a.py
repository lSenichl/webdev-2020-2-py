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
temp = 0

with open(comands, 'r') as file:
    for file_lines in file:
        if file_lines.find('!') == -1:
          for i in ignore:
            if file_lines.find(i) != -1:
              temp = temp + 1
          if temp == 0:
            print(file_lines.strip('\n'))
        temp = 0