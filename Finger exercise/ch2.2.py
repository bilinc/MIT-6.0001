# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:52:14 2020

@author: Bilin C
"""

x, y, z = 0, 2, 1

if not(x%2 == 0) and not(y%2 == 0) and not(z%2 == 0):
    if x > y and x > z:
        print('x is the largets:', x)
    elif y > z:
        print('y is the largest:', y)
    else:
        print('z is the largest:', z)
elif not(x%2 == 0) and not(y%2 == 0):
    if x > y:
        print('x is the largest:', x)
    else:
        print('y is the largest:', y)
elif not(y%2 == 0) and not(z%2 == 0):
    if y > z:
        print('y is the largest:', y)
    else:
        print('z is the largest:', z)
elif not(x%2 == 0) and not(z%2 == 0):
    if x > z:    
        print('x is the largest:', y)
    else:
        print('z is the largest:', z)
elif not(x%2 == 0):
    print('x is the largest:', x)
elif not(y%2 == 0):
    print('y is the largest:', y)
elif not(z%2 == 0):
    print('z is the largest:', z)
else:
    print('none of the numbers x, y and z are odd: x=%d, y=%d, z=%d' % (x,y,z))