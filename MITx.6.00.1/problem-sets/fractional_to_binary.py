# -*- coding: utf-8 -*-
"""
Created on Thu May 15 14:32:00 2025

@author: fbent
"""

x = float(input("Enter a decimal number between 0 and 1:\n"))

p = 0
while ((2**p) * x) % 1 != 0: # tells us how many binary places we need to fully represent x with finite precision
    print("Remainder = " + str((2**p) * x - int((2**p) * x))) 
    p += 1

    num = int(x * (2**p)) # convert the scaled up number to an integer

    result = ""
    if num == 0:  
        result = "0"

    while num > 0:
        result = str(num%2) + result
        num = num // 2 

    for i in range(p - len(result)): # Add leading zeros if needed 
        result = "0" + result

    result = result[0:-p] + "."  + result[-p:]

print(f"The binary respresentation of the decimal {x} is {result}")