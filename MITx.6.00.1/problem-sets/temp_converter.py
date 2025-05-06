# Temperature Converter with Error Handling
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (9/5) * celsius + 32
    print("Temperature in Fahrenheit is:", fahrenheit)
except ValueError:
    print("❌ Invalid input. Please enter a number, like 25 or -3.5")
