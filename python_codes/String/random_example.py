# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:07:31 2023

@author: admin
"""

import random

name = input('Enter your Name: ')

def val(name):
    return f'Welcome back {name}, Great to have you again...'
    
q1 = 'A new day is a new start'
q2 = 'Failures are the stepping stones for success'
q3 = 'Aim for stars'
q4 = 'It\'s not about what the story is, its about how it is narrated'

quotes = [q1, q2, q3, q4]

print(val(name))  # Now this will print the welcome message returned by val(name)
print(random.choice(quotes))

