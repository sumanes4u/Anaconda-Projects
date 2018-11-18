# Credit Card Calculation Program (Stage 2 with Error)

def displayWelcome():
    print('This program will determine the time to pay off a credit')
    print('card and the interest paid based on the current balance,')
    print('the interest rate, and the monthly payments made.')
     
def displayPayments(balance, int_rate, monthly_payment):

    # init
    num_months = 0
    total_int_paid = 0

    # display loan info
    print('PAYOFF SCHEDULE')
    print('\nCredit card balance: $' + format(balance,'.2f'))
    print('Annual interest rate:', str(1200 * int_rate)+'%')
    print('Monthly payment: $', format(monthly_payment,'.2f'))

    # display year-by-year account status
    while balance > 0:
        monthly_int = balance * int_rate
        total_int_paid = total_int_paid + monthly_int
        balance = balance + monthly_int - monthly_payment
            
        year = (num_months // 12) + 1
        print(year, format(balance,'.2f'), format(total_int_paid,'.2f'))

        num_months = num_months + 1
      
# ---- main

# display welcome screen
displayWelcome()

# determine current balance and APR
balance = int(input('\nEnter the balance on your credit card: '))
apr = int(input('Enter the annual interest rate (APR) on the card: '))
monthly_int_rate = apr/1200

# determine monthly payment
response = input('Use the minimum monthly payment? (y/n): ')

if response in ('y','Y'):
    if balance < 1000:
        monthly_payment = 20
    else:
        monthly_payment = balance * .02
else:
    monthly_payment = input('Enter monthly payment: ')
                
# display monthly payoff
displayPayments(balance, monthly_int_rate, monthly_payment)
