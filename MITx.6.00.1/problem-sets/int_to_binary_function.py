# -*- coding: utf-8 -*-
"""
Created on Wed May 14 21:16:27 2025

@author: fbent
"""

def int_to_binary(num):
    isNeg = num < 0
    num = abs(num)
    
    if num == 0:
        return '0'
    
    result = ''
    
    while num > 0:
        result = str(num%2) + result
        num = num//2
        
    if isNeg:
        result = "-" + result
        
    return result

# How to use 
if __name__ == "__main__":
    try:
        num = int(input("Which whole number would you like to turn into binary?\n"))
        print("Binary representation:", int_to_binary(num))
    except:
        print("⚠️ Please enter a valid whole number!")