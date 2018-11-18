# Phone Number Spelling Program

def getPhoneNum():

    """Returns entered phone number in the form 123-456-7890."""
    
    # init
    valid_ph_num = False
    empty_str = ''
    
    # prompt for phone number
    while not valid_ph_num:
        phone_num = input('Enter phone number (xxx-xxx-xxxx): ')
        
        # check if valid form
        if len(phone_num) != 12 or phone_num[3] != '-' or \
           phone_num[7] != '-':
            print ('INVALID ENTRY - Must be of the form xxx-xxx-xxxx\n')
        else:
        # check for non-digits
            k = 0
            valid_ph_num = True
            phone_num_digits = phone_num.replace('-', empty_str)
            
            while valid_ph_num and k < len(phone_num_digits):
                if not phone_num_digits[k].isdigit():
                    print('* Non-digit:', phone_num_digits[k],'*\n')
                    valid_ph_num = False
                else:
                    k = k + 1

    return phone_num

def displayAllSpellings(phone_num):

    """Displays all possible phone numbers with the last four digits
       replaced with a corresponding letter from the phone keys
    """

    translate = {'0': '0', '1':'1', '2': ('a','b','c'), '3': ('d','e','f'),
             '4': ('g','h','i'),'5': ('j','k','l'), '6': ('m','n','o'),
             '7': ('p','q','r','s'),'8': ('t','u','v'), '9': ('w','x','y','z')}

    # display spellings
    for let1 in translate[phone_num[8]]:
        for let2 in translate[phone_num[9]]:
            for let3 in translate[phone_num[10]]:
                for let4 in translate[phone_num[11]]:
                    print (phone_num[0:8] + let1 + let2 + let3 + let4)

#---- main

# program welcome
print ('This program will generate all possible spellings of the')
print ('last four digits of any phone number\n')

# get phone number and display spellings
terminate = False

while not terminate:

    phone_num = getPhoneNum()
    displayAllSpellings(phone_num)

    # continue?
    response = input('Enter another phone number? (y/n): ')
    if response == 'n':
        terminate = True
