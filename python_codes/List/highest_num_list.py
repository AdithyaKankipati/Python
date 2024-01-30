# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:42:06 2024

@author: admin
"""

user_list = []
len_list = int(input('Enter the length of the list: '))

for i in range(len_list):
    input_num = int(input('Enter the numbers: '))
    user_list.append(input_num)
print(f'The list is {user_list}')
sorted(user_list)
print(f'The largest number in the list is {user_list[-1]}')