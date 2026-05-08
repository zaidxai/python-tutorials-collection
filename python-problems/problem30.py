# Program to convert temperature from Fahrenheit to Centigrade (Celsius)

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

centigrade = 5 * (fahrenheit - 32) / 9

print(f"The temperature in Centigrade is: {centigrade:.2f}°C")