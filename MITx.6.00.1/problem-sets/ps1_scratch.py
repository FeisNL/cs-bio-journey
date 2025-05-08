# PS1 Q1 - Newton-Raphson method for square root
# Find square root of a number using iterative improvement

# Number to find square root of
a = 25
# Initial guess
guess = a / 2.0
# How close we want to get
epsilon = 0.01
# Step counter (just to show how fast it converges)
steps = 0

while abs(guess**2 - a) >= epsilon:
    guess = guess - (((guess ** 2) - a) / (2 * guess))
    steps += 1

print("Estimated square root of", a, "is", guess)
print("Number of steps:", steps)