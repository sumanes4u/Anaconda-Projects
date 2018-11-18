# Temperature Conversion Program (Fahrenheit to Celsius)

# This program will convert a temperature entered in Fahrenheit
# to the equivalent degrees in Celsius

# program greeting
print('This program will convert degrees Fahrenheit to degrees Celsius')

# get temperature in Fahrenheit
fahrenheit = float(input('Enter degrees Fahrenheit: '))

# calc degrees Celsius
celsius = (fahrenheit - 32) * 5 / 9

# output degrees Celsius
print(fahrenheit, 'degrees Fahrenheit equals',
       format(celsius, '.1f'), 'degrees Celsius')


