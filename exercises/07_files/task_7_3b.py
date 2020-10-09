# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input('Введите VLAN: ')

with open('CAM_table.txt', 'r') as file:
    temp_list = []
    temp_list2 = []

    for file_lines in file:
        if file_lines.find('/') != -1:
            temp_list2.append(int(file_lines.strip('\n').split()[0]))
            temp_list2.append(file_lines.strip('\n').split()[1])
            temp_list2.append(file_lines.strip('\n').split()[3])
            temp_list.append(temp_list2)
            temp_list2 = []

    temp_list.sort()

    for i in range(len(temp_list)):
        if str(temp_list[i][0]) == vlan:
            print(str(temp_list[i][0]) + '\t' + temp_list[i][1] + '\t' + temp_list[i][2])