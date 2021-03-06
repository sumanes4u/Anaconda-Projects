# Temperature Conversion Program (Celsius-Fahrenheit / Fahrenheit-Celsius)

# Display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

# Get temperature to convert
which = input('Enter selection: ')
temp = int(input('Enter temperature to convert: '))

# Determine  temperature conversion needed and display results
if which == 'F':
    converted_temp = format((temp - 32) * 5.0/9.0, '.1f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
    if which == 'C':
        converted_temp = format((9.0/5.0 * temp) + 32, '.1f')
        print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
    else:
        print('INVALID INPUT')
