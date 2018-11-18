import re
#Oct 28 12:20:44  cli[4141]: <341004> <WARN> |AP suman-hardening@1.2.3.5 cli|  Set amp discover allowed: code: fail-prov-no-shipped.
#text = 'Oct 28 12:20:44  cli[4141]: <341004> <WARN> |AP suman-hardening@1.2.3.5 cli|  Set amp discover allowed: code: fail-prov-no-shipped.'
pattern = r'(?P<month>\b[a-zA-Z]{3}\b) (?P<date>\b[\d]{1,2}\b) (?P<timestamp>\b[\d:]+\b)  (?P<error>[a-zA-Z]+\[[\d]+\]:) (?P<msgtype>\<[\d]+\>) (?P<msg>.+)'
#match = re.search(pattern,text)
#print(match.group('error'))


reo = re.compile(pattern)

fh = open('iap-error-logs.txt','r')
data = {}

for line in fh:
    m = reo.search(line)
    if m:
        errorlist = data.get(m.group('error'),None)
        if not errorlist:
            data[m.group('error')]=[m.group('msg')]
        else:
            data[m.group('error')].append(m.group('msg'))

#print (data)            

for i in data.keys():
    print (i,len(data[i]),data[i][0])
    #print (data[i][0])    
fh.close()
