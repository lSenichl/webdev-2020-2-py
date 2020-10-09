# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Введите IP: ')

try:
   if int(ip.split('.')[0]) not in list(range(0,256)) or int(ip.split('.')[1]) not in list(range(0,256)) or int(ip.split('.')[2]) not in list(range(0,256)) or int(ip.split('.')[3]) not in list(range(0,256)):
      print('Неправильный IP-адрес')
   elif int(ip.split('.')[0]) in list(range(1,224)):
      print('unicast')
   elif int(ip.split('.')[0]) in list(range(224,240)):
      print('multicast')
   elif ip.split('.') == ['255','255','255','255']:
      print('local broadcast')
   elif ip.split('.') == ['0','0','0','0']:
      print('unassigned')
   else:
      print('unused')
except IndexError:
   print('Неправильный IP-адрес')
except ValueError:
   print('Неправильный IP-адрес')