# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:04:39 2024

@author: admin
"""

def NameAge(Name,Age):
    return f'Nice to meet you {Name} and it\'s good to know that you are {Age} years old' 

print('Please enter your name and Age')
user_name = input('Enter your name: ')
user_age = int(input('Enter your Age: '))
print(NameAge(user_name, user_age))