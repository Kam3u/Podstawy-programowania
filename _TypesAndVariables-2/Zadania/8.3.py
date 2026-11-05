###
# A program that reads temperature in degrees Celsius from the keyboard
# and calculates temperature in Kelvin and Fahrenheit.
#
# read temperature in Celsius
celsius = float(input('Enter temperature in Celsius: '))

# convert Celsius to Kelvin and Fahrenheit
kelvin = celsius + 273.15
fahrenheit = (celsius * 9 / 5) + 32

# print results
print(f'Temperature in Kelvin: {kelvin:.2f} K')
print(f'Temperature in Fahrenheit: {fahrenheit:.2f} F')
