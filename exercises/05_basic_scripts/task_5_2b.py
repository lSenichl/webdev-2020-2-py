# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

#ip = input('IP: ')

ip = argv[1]

print('Network:')
ip2 = "{:08b}{:08b}{:08b}{:08b}".format(
    int(ip.split('/')[0].split('.')[0]), 
    int(ip.split('/')[0].split('.')[1]), 
    int(ip.split('/')[0].split('.')[2]),
    int(ip.split('/')[0].split('.')[3])
)

ip2 = ip2[:-(str("1" * (32 - int(str(ip.split('/')[1])))).count('1'))] + "0" * ((str("1" * (32 - int(str(ip.split('/')[1])))).count('1')))

print("{:<8} {:<8} {:<8} {:<8}".format(
    int(ip2[0:8], 2), 
    int(ip2[8:16], 2), 
    int(ip2[16:24], 2),
    int(ip2[24:32], 2)
))

print("{:8} {:8} {:8} {:8}".format(
    ip2[0:8], 
    ip2[8:16], 
    ip2[16:24],
    ip2[24:32]
), '\n')

print('Mask:')
print('/' + str(ip.split('/')[1]))
print("{:<8} {:<8} {:<8} {:<8}".format(
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[0:8], 2),
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[8:16], 2),
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[16:24], 2),
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[24:32], 2)
))
print("{:08b} {:08b} {:08b} {:08b} ".format(
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[0:8], 2),
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[8:16], 2),
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[16:24], 2),
    int(("1" * int(str(ip.split('/')[1])) + "0" * (32 - int(str(ip.split('/')[1]))))[24:32], 2)
))