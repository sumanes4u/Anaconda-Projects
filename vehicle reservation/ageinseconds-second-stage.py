# Age in Seconds Program

import datetime

# This program will calculate a person's approximate age in seconds

### Get month, day, year of birth
##month_birth = int(input('Enter month born (1-12): '))
##day_birth = int(input ('Enter day born (1-31): '))
##year_birth = int(input('Enter year born (4-digit): \n'))
##
### Get current month, day, year
##current_month = datetime.date.today().month
##current_day = datetime.date.today().day
##current_year = datetime.date.today().year

# Determine number of seconds in a day, average month, and average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# Test output
print ('numsecs_day ', numsecs_day)
print ('avg_numsecs_month = ', avg_numsecs_month)
print ('avg_numsecs_year = ', avg_numsecs_year)

