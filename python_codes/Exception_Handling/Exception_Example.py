# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:54:37 2024

@author: admin
"""

try:
    user_input1 = int(input('Enter first number: '))
    user_input2 = int(input('Enter second number: '))

    if user_input1 > user_input2:
        print(f'{user_input1} is higher than {user_input2}')
    elif user_input1 < user_input2:
        print(f'{user_input2} is higher than {user_input1}')
    else:
        print('Both the numbers are the same')

except ValueError:
    print('Please enter valid integers and not float, string, etc.')
