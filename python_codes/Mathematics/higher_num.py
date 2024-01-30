# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:23:26 2024

@author: admin
"""

def HighNum(num1,num2):
    if num1 > num2:
        print(f'{num1} is the higher number')
    elif num1 < num2:
        print(f'{num2} is the higher number')
    else:
        print('Both the numbers are same')

user_input1 = int(input('Enter the first number: '))
user_input2 = int(input('Enter the second number: '))
HighNum(user_input1, user_input2)