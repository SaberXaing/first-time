# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 20:54:59 2021

@author: eddy9111226
"""

year=int(input())
while (year!=-9999):
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        print("yes")
    else:
        print("no")
    year=int(input())






