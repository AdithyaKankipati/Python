# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:38:58 2024

@author: admin
"""
import random as rn

low_num = int(input('Enter the lower number: '))
high_num = int(input('Enter the Higher number: '))

actual_num = rn.randint(low_num, high_num)
print('Guess the Number in 3 chances')

for _ in range(4):  # Loop for three chances
    expected_num = int(input('Enter your guess: '))
    
    if expected_num == actual_num:
        print(f'Congratulations! You have guessed correctly. The number is {actual_num}')
        break  # Exit the loop if the guess is correct
    elif expected_num < actual_num:
        print('Too close, But the number is higher.')
    elif expected_num > actual_num:
        print('Too close, But the number is lower.')
    else:
        print('Incorrect guess, Try again')

