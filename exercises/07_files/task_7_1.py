# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('c:\\Users\\barys\\web-2020-2\\webdev-2020-2-py\\exercises\\07_files\\ospf.txt', 'r') as text:
    ospf = text.readlines()

    for file_lines in ospf:
        new_line = file_lines.strip().split()

        prefix = new_line[1]
        ad_metric = new_line[2].strip('[]')
        next_hop = new_line[4].strip(',')
        last_update = new_line[5].strip(',')
        outbound_interface = new_line[6]

        ospf_route = """
        Prefix:               {0:18}
        AD/Metric:            {1:18}
        Next-Hop:             {2:18}
        Last update:          {3:18}
        Outbound Interface:   {4:18}
        """

        print(ospf_route.format(prefix,ad_metric,next_hop,last_update,outbound_interface))