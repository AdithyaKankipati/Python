# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:22:51 2024

@author: admin
"""
word_input = input('Enter a word to check whether it\'s a palindrome or not: ')
i = 0
j = len(word_input) - 1

while i < j:
    if word_input[i] != word_input[j]:
        print(f"{word_input} is not a palindrome.")
        break
    i += 1
    j -= 1
else:
    print(f"{word_input} is a palindrome.")
