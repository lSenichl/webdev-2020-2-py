# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access_config = {}
    trunk_config = {}
    
    with open(config_filename, 'r') as file:
        for line in file:
            if line.find('FastEthernet') != -1:
                interface = line.split()[-1]
                line = file.readline()

                if line.find('mode access') != -1:
                    line = file.readline()
                    access_vlan = line.split()[-1]

                    if access_vlan.isdigit():
                        access_config[interface] = int(access_vlan)
                    else:
                        access_config[interface] = 1

                elif line.find('encapsulation dot1q') != -1:
                    line = file.readline()
                    trunk_vlan_temp = line.split()[-1].split(',')
                    trunk_vlan = []

                    for i in trunk_vlan_temp:
                        trunk_vlan.append(int(i))

                    trunk_config[interface] = trunk_vlan

        return access_config, trunk_config