# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

def convert_ranges_to_ip_list(list_of_ips_and_ranges):
    ip = []

    for nip in list_of_ips_and_ranges:
        print(nip)
        if nip.find('-') != -1: 
            first_ip = nip.split('-')[0]
            last_octet_of_first_ip = int(first_ip.split('.')[-1])

            if nip.count('.') < 4:
                last_octet_of_second_ip = int(nip.split('-')[-1])
            else:
                last_octet_of_second_ip = int(nip[nip.rfind('.')+1:])

            first_three_octets_of_ip = first_ip[:first_ip.rfind('.')+1]
            
            for new_ip in range(last_octet_of_first_ip, last_octet_of_second_ip + 1):
                ip.append(first_three_octets_of_ip + str(new_ip))

        else:
            ip.append(nip)

    return ip