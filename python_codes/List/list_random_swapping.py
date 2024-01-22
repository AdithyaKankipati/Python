# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:53:03 2024

@author: admin
"""

user_list = [1, 2, 3, 4, 5]
print(f'The list is {user_list}')

input_one = int(input('Enter first position: '))
input_two = int(input('Enter second position: '))

# Validate inputs to ensure they are within the range of the list indices
if 1 <= input_one <= len(user_list) and 1 <= input_two <= len(user_list):
    # Swap the elements at the specified positions
    user_list[input_one - 1], user_list[input_two - 1] = user_list[input_two - 1], user_list[input_one - 1]
    print(f'After swapping, the list is {user_list}')
else:
    print('Invalid input positions. Please enter valid positions.')
