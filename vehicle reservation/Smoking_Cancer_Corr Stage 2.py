# Smoking/Cancer Correlation Program

# program greeting
print ('This program will determine the correlation (-1 to 1) between')
print ('data on cigarette smoking and incidences of lung cancer\n')

# init
smoking_datafile_opened = False
cancer_datafile_opened = False
num_attempts = 0
max_attempts = 6

# open input files
while ((not smoking_datafile_opened) and (not cancer_datafile_opened)) \
       and (num_attempts < max_attempts):
    try:
        if not smoking_datafile_opened:
            file_name = input('Enter file name with smoking data: ')
            smoking_datafile = open(file_name, 'r')
            smoking_datafile_opened = True
        
        if not cancer_datafile_opened:
            file_name = input('Enter file name with lung cancer data: ')
            cancer_datafile = open(file_name, 'r')
            cancer_datafile_opened = True
        
    except IOError:
        print ('File not found - please reenter\n')
        num_attempts = num_attempts + 1

if not smoking_datafile_opened or not cancer_datafile_opened:
    print('Too many attempts of input file name\nProgram terminated') 
else: 
    # read past file headers
    smoking_datafile.readline()
    cancer_datafile.readline()

    # init empty lists
    smoking_data = []
    cancer_data = []
    
    for k in range(1,6):
        s_line = smoking_datafile.readline()
        smoking_data.append(s_line.strip().split(','))
        c_line = cancer_datafile.readline()
        cancer_data.append(c_line.strip().split(','))

    print('Smoking Data:', smoking_data)
    print('\nCancer Data:', cancer_data)
