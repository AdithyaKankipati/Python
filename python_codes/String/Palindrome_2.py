# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:55:09 2024

@author: admin
"""

user_input = input('Enter any word and check whether it/''s a palindrome or not: ')

if user_input.upper() == user_input[::-1].upper():
    print('The given word is a palindrome')
else:
    print('Sorry, The word is not a palindrome')