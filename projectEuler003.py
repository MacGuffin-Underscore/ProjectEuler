# -*- coding: utf-8 -*-
"""
projectEuler003.py

@author: MacGuffin_

Created on Wed Jun 16 09:29:12 2021
---------------------------------------------------------------------------
Problem Statement:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np

num = 600851475143

for i in range(3,round(np.sqrt(num))):
    while num % i == 0:
        maxPF = i
        num = num / i
            
print(maxPF)