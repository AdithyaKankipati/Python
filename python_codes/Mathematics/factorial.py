# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:11:53 2024

@author: admin
"""

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
num = int(input('Enter any number: '))
print("Factorial of",num,"is",
factorial(num))