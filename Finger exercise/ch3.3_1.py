# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:52:14 2020

@author: Bilin C
"""

x = -25
epsilon = 0.01
numGuesses = 0
low = min(0.0, x)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - abs(x)) >= epsilon:
    print('low = ', low, 'high = ', high, 'ans = ', ans)
    numGuesses += 1
    if ans**2 < abs(x):
        high = ans
    else:
        low = ans
    
    ans = (high + low)/2
print('numGuesses = ', numGuesses)
print(ans, 'is close to square root of', x)
