# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:01:06 2024

@author: admin
"""

data_list = []

list_size = int(input('Enter size of the list: '))

for i in range(list_size):
    data_num = int(input(f'Enter {list_size-i} numbers: '))
    data_list.append(data_num)

print(data_list)

sorted_list = sorted(data_list)
print(f'Sorted sequence for the given list is {sorted_list}')