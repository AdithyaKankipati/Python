# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:43:45 2024

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

# Selection Sort Implementation
for i in range(list_len):
    min_index = i
    for j in range(i + 1, list_len):
        if user_list[j] < user_list[min_index]:
            min_index = j

    # Swap the found minimum element with the first element
    user_list[i], user_list[min_index] = user_list[min_index], user_list[i]

# Print sorted list
print("Sorted List (using Selection Sort):", user_list)
