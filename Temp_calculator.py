# Temperature Converter in python

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    return kelvin


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    return fahrenheit


print("**** Temperature Converter ****")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter the above number to Convert :- "))

if choice == 1:
    celsius = float(input("Enter Temperature in Celsius :- "))
    print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(celsius))

elif choice == 2:
    celsius = float(input("Enter Temperature in Celsius :- "))
    print("Temperature in kelvin: ", celsius_to_kelvin(celsius))

elif choice == 3:
    fahrenheit = float(input("Enter Temperature in Fahrenheit :- "))
    print("Temperature in Celsius: ", fahrenheit_to_celsius(fahrenheit))

elif choice == 4:
    fahrenheit = float(input("Enter Temperature in Fahrenheit :- "))
    print("Temperature in kelvin: ", fahrenheit_to_kelvin(fahrenheit))

elif choice == 5:
    kelvin = float(input("Enter Temperature in Kelvin :- "))
    print("Temperature in Celsius: ", kelvin_to_celsius(kelvin))

elif choice == 6:
    kelvin = float(input("Enter Temperature in Kelvin :- "))
    print("Temperature in Fahrenheit: ", kelvin_to_fahrenheit(kelvin))

else:
    print("Invalid Choice")
