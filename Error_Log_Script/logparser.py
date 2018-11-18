import re

#[Fri Oct 28 05:43:38.294803 2016] [ssl:warn] [pid 4500:tid 304] AH01909: www.example.com:443:0 server certificate does NOT include an ID which matches the server name

p=r'^\[(?P<day>[a-zA-z]{3}) (?P<month>[a-zA-z]{3}) (?P<date>[\d]{1,2}) (?P<timestamp>\b[\d:\.]+\b) (?P<year>[\d]{4})\] \[(?P<error>[\w:]+)\] \[(?P<who>[\w: ]+)\] (?P<msg>.+)$'

reo = re.compile(p)
fh = open('tmp.txt')

data ={}

for line in fh:
    m = reo.search(line)
    if m:
        error_list = data.get(m.group('error'), None)
        #print(error_list)
        if not error_list:
            data[m.group('error')]=[m.group('msg')]
        else:
            data[m.group('error')].append(m.group('msg'))

print (data)

#print data['core:warn']
for i in data.keys():
    print (i, len(data[i]))
	
fh.close()
