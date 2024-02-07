# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 08:07:40 2024

@author: admin
"""

def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

input1 = int(input('Enter a number: '))
input2 = int(input('Enter another number: '))

output = add(input1, input2)

print(f'Addition of {input1} + {input2} is {output}')


