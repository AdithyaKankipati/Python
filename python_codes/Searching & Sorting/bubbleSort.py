# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:32:09 2024

@author: admin
"""

user_list = []
list_len = int(input(('Enter the size of the list: ')))

for i in range(list_len):
    user_input = int(input('Enter the numbers to add in the list: '))
    user_list.append(user_input)
print(user_list)
for j in range(list_len):
    for k in range(0,list_len-j-1):
        if user_list[k] > user_list[k+1]:
            user_list[k], user_list[k+1] = user_list[k+1], user_list[k]
print(user_list)