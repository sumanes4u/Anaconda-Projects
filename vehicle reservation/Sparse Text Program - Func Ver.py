# Sparse Text Program

def createModifiedFile(input_file, outputfile):
    '''
        For text file input_file, creates a new version in file outputfile
        in which all instances of the letter 'e' are removed.
    '''
    
    empty_str = ''
    num_total_chars = 0
    num_removals = 0

    for line in input_file:
    
        # save original line length
        orig_line_length = len(line) - 1
        num_total_chars = num_total_chars + orig_line_length
        
        # remove all occurrances of letter 'e'
        modified_line = line.replace('e',empty_str).replace('E',empty_str)
        num_removals = num_removals + \
                         (orig_line_length - (len(modified_line)-1))

        # simulataneouly output line to screen and output file
        print(modified_line.strip('\n'))
        output_file.write(modified_line)

    return (num_total_chars, num_removals)

# --- main

# program welcome
print("This program will display the contents of a provided text file")
print("with all occurrences of the letter 'e' removed.\n")

# open files for reading and writing
file_name = input('Enter file name (including file extension): ')
input_file = open(file_name,'r')
new_file_name = 'e_' + file_name
output_file = open(new_file_name,'w')

# create file with all letter e removed
print()
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# close current input and output files
input_file.close()
output_file.close()

# display percentage of characters removed
print()
print(num_removals, "occurrences of the letter 'e' removed")
print('Percentage of data lost:',
      int((num_removals / num_total_chars) * 100), '%')
print('Modified text in file', new_file_name)
    
