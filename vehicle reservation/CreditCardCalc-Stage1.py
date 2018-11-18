# Credit Card Calculation Program (Stage 1)

def displayWelcome():
    print('\n.... Entering function display welcome')
     
def displayPayments(balance, int_rate, monthly_payment):
    print('\n.... Entering function displayPayments')
    print('parameter balance =', balance)
    print('parameter int_rate =', int_rate)
    print('parameter monthly_payment =', monthly_payment)
        
# ---- main

# display welcome screen
displayWelcome()

# get current balance and APR
balance = int(input('\nEnter the balance on your credit card: '))
apr = int(input('Enter the interest rate (APR) on the card: '))
monthly_int_rate = apr/1200

# determine monthly payment
response = input('Use the minimum monthly payment? (y/n): ')

if response in ('y','Y'):
    print('Minimum payment selected')
    monthly_payment = 20
else:
    print('User-entered monthly payments selected')
    monthly_payment = input('Enter monthly payment: ')
                
# display monthly payoff
displayPayments(balance, monthly_int_rate, monthly_payment)
