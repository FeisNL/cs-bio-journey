# temperature converter - 2 directions

print("What kind of temperature do you like to convert?")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter 1 or 2: \n")

try:
    if choice == "1":
        c = float(input("Enter temperature in celcius: \n"))
        f = (9/5) * c + 32
        print("Fahrenheit:", f)
    elif choice == "2":
        f = float(input("Enter temperature in Farhrenheit: \n"))
        c = (5/9) * (f-32)
        print("Celcius:", c)
    else:
        print("❌ Invalid option. Please enter 1 or 2.")

except ValueError:
    print("❌ Invalid temperature input. Please enter a valid number.")


