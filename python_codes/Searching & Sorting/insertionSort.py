# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:50:36 2024

@author: admin
"""

user_list = []
list_len = int(input('Enter the size of the list: '))

# Get user input to populate the list
for i in range(list_len):
    user_input = int(input('Enter the numbers to add in the list: '))
    user_list.append(user_input)

# Print unsorted list
print("Unsorted List:", user_list)

# Insertion Sort Implementation
for i in range(1, list_len):
    key = user_list[i]
    j = i - 1

    while j >= 0 and key < user_list[j]:
        user_list[j + 1] = user_list[j]
        j -= 1

    user_list[j + 1] = key

# Print sorted list
print("Sorted List (using Insertion Sort):", user_list)
