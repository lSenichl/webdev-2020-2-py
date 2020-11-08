# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def ping_ip_addresses(list_of_ips):

    rreply = []
    wreply = []

    for nip in list_of_ips:

        reply = subprocess.run(['ping', nip])
        if reply.returncode == 0:
            rreply.append(nip)
        else:
            wreply.append(nip)

    result = (rreply, wreply)
    
    return result


