# Temperature Display Program (List Version)

daily_temps = [68.8, 70.2, 67.2, 71.8, 73.2, 75.6, 74.0]

print('This program will display the average temperature for a given day')
terminate = False

while not terminate:

    day = input('Enter day (sun, mon, tue, wed, thur, fri, sat): ')

    if day == 'sun':
        dayname = 'Sunday'
        temp = daily_temps[0]
    elif day == 'mon':
        dayname = 'Monday'
        temp = daily_temps[1]
    elif day == 'tue':
        dayname = 'Tuesday'
        temp = daily_temps[2]
    elif day == 'wed':
        dayname = 'Wednesday'
        temp = daily_temps[3]
    elif day == 'thur':
        dayname = 'Thursday'
        temp = daily_temps[4]
    elif day == 'fri':
        dayname = 'Friday'
        temp = daily_temps[5]
    elif day == 'sat':
        dayname = 'Saturday'
        temp = daily_temps[6]

    print('The average temperature for', dayname, 'was', temp, 'degrees\n')

    response = input('Continue with another day? (y/n): ')
    if response == 'n':
        terminate = True
