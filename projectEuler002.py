# -*- coding: utf-8 -*-
"""
projectEuler002.py

@author: MacGuffin_

Created on Tue Jun 15 22:10:00 2021
---------------------------------------------------------------------------
Problem Statement:
    
Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
"""
import numpy as np

mx = 4000000            # Maximum number in the sequence
fib = np.array([1,2])   # Start sequence at 1, 2
even = 2                # Sum must include original even value(s)
while fib[1] < mx:
    out = fib[0] + fib[1]
    if out % 2 == 0:
        even += out
    fib[0] = fib[1]     # slide value down
    fib[1] = out        # insert new value

print(even)