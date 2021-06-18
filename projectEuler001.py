# -*- coding: utf-8 -*-
"""
projectEuler001.py

@author: MacGuffin_

Created on Tue Jun 15 21:41:06 2021
---------------------------------------------------------------------------
Problem Statement:
    
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
n = 1000
mults = 0

for i in range(n):
    if float(i/3).is_integer() or float(i/5).is_integer():
        mults += i 
        
print(mults)