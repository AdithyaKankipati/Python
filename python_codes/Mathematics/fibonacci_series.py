# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:32:48 2024

@author: admin
"""

user_input = []
list_len = int(input('Enter range of the series: '))

for i in range(list_len):
    if i < 2:
        user_input.append(i)
    else:
        user_input.append(user_input[-1] + user_input[-2])

# Convert the user_input list to a string
final_output = ' '.join(map(str, user_input))

# Replace spaces with commas
final_output = final_output.replace(' ', ',')

# Display the output
print(final_output)

