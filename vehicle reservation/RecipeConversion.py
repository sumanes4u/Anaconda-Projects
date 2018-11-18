# Recipe Conversion Program


from fraction import *

def getFile():

    ''' Returns as a tuple the file name entered by the user and the
        open file object. If the file exceeds three attempts of opening
        sucessfully, an IO exception is raised.
    '''

    file_name = input('Enter file name: ')
    input_file_opened = False
    num_attempts = 1

    while not input_file_opened and num_attempts < 3:
        try:
            input_file = open(file_name, 'r')
            input_file_opened = True
        except IOError:
            print('File Open Error\n')
            num_attempts = num_attempts + 1
            file_name = input('Enter file name: ')

    if num_attempts == 3:
        raise IOError('Exceeded number of file open attempts')

    return (file_name, input_file)

def removeMeasure(line):

    ''' Returns provided line with any initial digits and fractions (and
        any surrounding blanks) removed. 
    '''

    k = 0
    blank_char = ' '
    
    while k < len(line) and (line[k].isdigit() or \
                             line[k] in ('/', blank_char)):
        k = k + 1

    return line[k:len(line)]

def scanAsFraction(line):

    ''' Scans all digits, including fractions, and returns as a Fraction
        object. For example, '1/2' would return as Fraction value 1/2,
        '2' would return as Fraction 1/2, and '2 1/2' would return as
        Fraction value 3/2.
    '''

    completed_scan = False
    value_as_frac = Fraction(0,1)
    
    while not completed_scan:
        k = 0
        while k < len(line) and line[k].isdigit():
            k = k + 1
            
        numerator = int(line[0:k])
        
        if k < len(line) and line[k] == '/':
            k = k + 1
            start = k
            while k < len(line) and line[k].isdigit():
                k = k + 1
                
            denominator = int(line[start:k])
        else:
            denominator = 1

        value_as_frac = value_as_frac + Fraction(numerator, denominator)

        
        if k == len(line):
            completed_scan = True
        else:  
            line = line[k:len(line)].strip()
            
            if not line[0].isdigit():
                completed_scan = True
            
    return value_as_frac

def convertLine(line, factor):

    ''' If line begins with a digit, then returns line with the value
        incremented by factor. Otherwise, returns line unaltered.
        (For example, for a factor of 2, '1/4 cup sugar' returns as
        '1/2 cup sugar and '2 cups sugar' returns as '4 cups sugar'.)
    '''

    if line[0].isdigit():
        blank_char = ' '
        frac_meas = scanAsFraction(line) * factor

        if frac_meas.getDenominator() == 1:
            frac_meas = frac_meas.getNumerator()
        
        conv_line = str(frac_meas) + blank_char + removeMeasure(line)
    else:
        conv_line = line

    return conv_line 


# ---- main

# display welcome
print('This program will convert a given recipe to a different')
print('quantity based on a specified conversion factor. Enter a')
print('factor of 1/2 to halve, 2 to double, 3 to triple, etc.\n')

try:

    # get file name and open file
    file_name, input_file = getFile()

    # get conversion factor
    conv_factor = input('Enter the conversion factor: ')
    conv_factor = scanAsFraction(conv_factor)

    # open output file named 'conv_' + file_name
    output_file_name = 'conv_' + file_name
    output_file = open(output_file_name, 'w')

    # convert recipe                  
    empty_str = ''
    recipe_line = input_file.readline()

    while recipe_line != empty_str:
        recipe_line = convertLine(recipe_line, conv_factor)
        output_file.write(recipe_line)
        recipe_line = input_file.readline()

    # close files
    input_file.close()
    output_file.close()

    # display completion message to user
    print('Converted recipe in file: ', output_file_name)

except IOError as err_mesg:  # catch file open error
    print(err_mesg)

