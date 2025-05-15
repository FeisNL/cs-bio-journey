# -*- coding: utf-8 -*-
"""
Created on Thu May 15 18:47:49 2025

@author: fbent
"""

def decimal_to_binary(x):
    """
    Convert a decimal number between 0 and 1 (exclusive) into its binary representation as a string.
    For example: 0.625 -> '0.101'
    """
    # Check: x must be greater than 0 and less than 1, if not raise ValueError
    if x <= 0 or x >= 1:
        raise ValueError("Input must be a decimal between 0 and 1")
        
    # step 1: determine how many binary places we need
    # Keep multiplying by powers of 2 until the result becomes (almost) a whole number.
    # This is necessary because some decimals like 0.1 cannot be exactly represented in binary — they repeat forever (like 1/3 in decimal).
    # We look for the smallest p such that (2^p) * x is a whole number or very close to one.
    p = 0
    while ((2**p) * x) % 1 != 0:
        p += 1
        
    # step 2: multiply by x to shift the decimal number into an integer
    num = int((2**p) *x)
    
    # step 3: converting an integer into a binary string
    result = ""
    if num == 0:
        result = '0'
    else:
        while num > 0:
            result = str(num%2) + result
            num = num // 2
            
    # step 4: pad leading zeros until its length is at least p
    result = result.zfill(p)
    
    # step 5: insert the binary point
    if p == len(result):
         result = "0." + result
    else:
        result  = result[0:-p] + "." + result[-p:]
        
    # returning result of executing the function
    return result
        
# example
if __name__ == "__main__":
    try:
        x = float(input("Enter a decimal number between 0 and 1: \n"))
        print("Binary representation: ",  decimal_to_binary(x))
    except ValueError as e:
        print("Error:", e)