# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:56:53 2024

@author: admin
"""

min_val = int(input('Enter first number in the list: '))
max_val = int(input('Enter last number in the list: '))
user_list = []
for i in range(min_val, (max_val)+1):
    user_list.append(i)
print(user_list)