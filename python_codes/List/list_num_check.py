# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:05:53 2024

@author: admin
"""

user_list = [1, 2, 3, 4, 5, 6]

check_num = int(input('Enter the number that you want to check whether it\'s in the list or not: '))

number_found = False

for i in user_list:
    if i == check_num:
        print(f'The number {check_num} is in the list.')
        number_found = True
        break

if not number_found:
    print(f'Sorry, the number {check_num} is not in the list. Would you like to add it?')
    
    user_input = input('Enter YES or NO: ')
    
    if user_input.upper() == 'YES':
        user_list.append(check_num)
        print(f'The number {check_num} has been added to the list.')
    else:
        print('No changes have been made to the list.')

print(f'The updated list is: {user_list}')
