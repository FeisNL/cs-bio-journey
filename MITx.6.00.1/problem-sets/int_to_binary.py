# -*- coding: utf-8 -*-
"""
Created on Wed May 14 15:45:35 2025

@author: fbent
"""

num = int(input("Which whole number would you like to convert into binary?"))

if num < 0:
    isNeg = True # we don't want negative numbers in the conversion loop, prepend later '-' to turn it back negative
    num = abs(num) # converts the number into an absolute value
else:
    isNeg = False
    
result = "" # initialzing empty string, to build on one digit at a time

if num == 0:
    result = "0"
    
while num > 0:
    result = str(num % 2) + result
    num = num // 2
    
if isNeg:
    result = "-" + result
    
print(f"\nThe result of turning {num} into binary is {result}")