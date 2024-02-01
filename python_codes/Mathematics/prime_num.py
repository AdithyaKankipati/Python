# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:06:18 2024

@author: admin
"""
user_input = int(input('Enter the number: '))

if user_input > 1:
    for i in range(2,user_input):
        if user_input%i == 0:
            print('The number is not a prime')
            break
        else:
            print('The number is a prime')
            break
else:
    print('Please enter a positive number')
