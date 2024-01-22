# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:59:06 2024

@author: admin
"""

user_list = []

list_size = int(input('Enter size of the list: '))

for i in range(list_size):
    data_num = int(input(f'Enter {list_size-i} numbers: '))
    user_list.append(data_num)

print(f'The list created is {user_list}')
new_list = user_list[::-1]
print(new_list)
