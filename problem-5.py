#5. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit.
# Take the Celsius temperature as input from the user.


def Celsius_to_Fahrenheit(Celsius):
    return ((Celsius*1.8)+32)

Celsius = float (input("Enter a celsius temperature: "))

Fahrenheit = Celsius_to_Fahrenheit(Celsius)

print(Fahrenheit)



