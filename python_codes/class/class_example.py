# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:39:53 2024

@author: admin
"""
class Name():
    att1 = ['She', 'He']
    
    def __init__(self, Name):
        self.Name = Name

Amy = Name("Rodger")
Tommy = Name("Tommy")
 
# Accessing class attributes
print("{} is Amy".format(Amy.__class__.att1[0]))
print("{} is Tommy".format(Tommy.__class__.att1[1]))

 