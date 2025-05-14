# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Please think of a number between 0 and 100!")

low = 0
high = 100

while True:
    guess = (low+high) / 2

    print(f"Is your secret number {guess} ?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    answer = input().lower()

    if answer == "h":
        high = guess
    elif answer == "l":
        low = guess
    else:
        if answer == "c":
            print(f"Your secret number was {guess}")
