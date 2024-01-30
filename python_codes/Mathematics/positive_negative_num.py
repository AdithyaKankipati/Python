# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:58:46 2024

@author: admin
"""

user_input = float(input('Enter the number: '))
if user_input < 0:
    print(f'{user_input} is a negative number')
elif user_input > 0:
    print(f'{user_input} is a positive number')
else:
    print(f'The number you entered is {user_input}, which neither a postive number nor a negative number')