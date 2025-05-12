# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def main():
    while True: # ✅ case sensitivity
        try:
            a = float(input("Enter a positive number to approximate its square root: "))
            if a <= 0:
                print("❌ Please enter a number greater than zero")
                continue
            break
        except ValueError:
            print("❌ That wasn't a valid number. Please try again")

    guess = a/2.0
    epsilon = 0.01
    steps = 0

    while abs(guess**2 - a) >= epsilon:
        guess = guess - (((guess ** 2) -a) / (2 * guess))
        steps += 1

    print(f"Estimated root of {a} is {guess}")
    print(f"Number of steps is {steps}")

if __name__ == "__main__":
    main()
