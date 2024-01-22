# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:49:11 2024

@author: admin
"""

def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]

print(newList)
print(swapList(newList))