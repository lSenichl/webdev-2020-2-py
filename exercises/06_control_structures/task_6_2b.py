# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
right_answer = 0

while not right_answer:
    ip = input('Введите IP: ')
    
    try:
        if int(ip.split('.')[0]) not in list(range(0,256)) or int(ip.split('.')[1]) not in list(range(0,256)) or int(ip.split('.')[2]) not in list(range(0,256)) or int(ip.split('.')[3]) not in list(range(0,256)):
            print('Неправильный IP-адрес')
        elif int(ip.split('.')[0]) in list(range(1,224)):
            print('unicast')
            right_answer = 1
        elif int(ip.split('.')[0]) in list(range(224,240)):
            print('multicast')
            right_answer = 1
        elif ip.split('.') == ['255','255','255','255']:
            print('local broadcast')
            right_answer = 1
        elif ip.split('.') == ['0','0','0','0']:
            print('unassigned')
            right_answer = 1
        else:
            print('unused')
            right_answer = 1
    except IndexError:
        print('Неправильный IP-адрес')
    except ValueError:
        print('Неправильный IP-адрес')