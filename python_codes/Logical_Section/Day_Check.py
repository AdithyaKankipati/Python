# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:52:20 2024

@author: admin
"""
DayList = {'1': 'Sunday', '2': 'Monday', '3': 'Tuesday',
           '4': 'Wednesday', '5': 'Thursday', '6': 'Friday',
           '7': 'Saturday'}

input1 = input('Enter current day: ')
input2 = int(input('Enter number of days: '))

current_day_index = list(DayList.keys())[list(DayList.values()).index(input1)]
next_day_index = (int(current_day_index) + input2) % 7

next_day_name = DayList[str(next_day_index)]

print(f'The day after {input2} days from {input1} is {next_day_name}')
 
    