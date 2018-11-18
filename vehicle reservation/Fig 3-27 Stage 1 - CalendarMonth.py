# Calendar Month Program (stage 1)

# init
terminate = False

# program greeting
print('This program will display a calendar month between 1800 and 2099')

while not terminate:
    # get month and year
    month = int(input('Enter month 1-12 (-1 to quit): '))
    
    if month == -1:
        terminate = True
    else:
        while month < 1 or month > 12:
            month = int(input('INVALID INPUT - Enter month 1-12: '))

        year = int(input('Enter year (yyyy): '))
        
        while year < 1800 or year > 2099:
            year = int(input('INVALID - Enter year (1800-2099): '))

        # determine if leap year
        if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
            leap_year = True
        else:
            leap_year = False

        # determine num of days in month
        if month in (1, 3, 5, 7, 8, 10, 12):
            num_days_in_month = 31
        elif month in (4, 6, 9, 11):
            num_days_in_month = 30
        elif leap_year:  # February
            num_days_in_month = 29
        else:
            num_days_in_month = 28
           
        print ('\n', month, ',', year, 'has', num_days_in_month, 'days')
        
        if leap_year:
            print (year, 'is a leap year\n')
        else:
            print (year, 'is NOT a leap year\n')
