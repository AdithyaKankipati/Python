# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:23:56 2024

@author: admin
"""
user_input = input('Enter any sentence and it is reversed: ')

reversed_input = user_input.split()[::-1]

input_list = []

for i in reversed_input:
    input_list.append(i)
print(' '.join(input_list))