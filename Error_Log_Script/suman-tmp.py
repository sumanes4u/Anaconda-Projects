import re
import sys
from sys import argv

#Oct 28 12:20:44  cli[4141]: <341004> <WARN> |AP suman-hardening@1.2.3.5 cli|  Set amp discover allowed: code: fail-prov-no-shipped.
pattern = r'(?P<month>[a-zA-Z]{3}) (?P<date>[\d]{1,2}) (?P<timestamp>\b[\d:]+\b)  (?P<error>[a-zA-Z]+\[[\d]+\]:) (?P<msg>.+)'

##print (len(sys.argv))
#arglength = len(sys.argv)
#print (arglength)
for args in sys.argv[1:]:
    print ('ARGUMENTS PASSED IS:',args)
    
if len(sys.argv) < 2:
    print('Usage:python suman-tmp.py <FileName>')
    sys.exit()
else:
    file_name = sys.argv[1]
    print ('Correct Syntax:',file_name)
    pass

print(file_name)
reo = re.compile(pattern)
data = {}

fh = open(file_name,'r')

for line in fh:
    match = reo.search(line)
    if match:
        errorlist = data.get(match.group('error'),None)
        if not errorlist:
            data[match.group('error')] = [match.group('msg')]
        else:
            data[match.group('error')].append(match.group('msg'))
            
print(data.keys())

for i in data.keys():
    print ('Pinting OP')
    print (i,len(data[i]))

fh.close()
