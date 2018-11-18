
# coding: utf-8

# In[2]:

import re


# In[3]:

string = 'This is a \nnormal string'


# In[4]:

print (string)


# In[5]:

rawstring = r'and this is a \nraw string'


# In[6]:

print (rawstring)


# In[7]:

# re.match()
# re.search()
# re.findall()
# re.finditer


# In[8]:

re.match(r'dog','dog cat dog')


# In[9]:

match = re.match(r'dog','dog cat dog')


# In[10]:

match


# In[11]:

match.group(0)


# In[12]:

re.match(r'cat','dog cat dog')


# In[13]:

match2 = re.search(r'cat','dog cat dog')


# In[14]:

match2.group(0)


# In[15]:

re.findall(r'dog','dog cat dog')


# In[16]:

re.findall(r'cat','dog cat dog')


# In[17]:

match = re.search(r'dog','dog cat dog')


# In[18]:

match.start()


# In[19]:

match.end()


# In[20]:

match2 = re.search(r'cat','dog cat dog')


# In[21]:

match2


# In[22]:

match2.start()


# In[23]:

match2.end()


# In[24]:

match = re.match(r'dog','dog cat dog')
print (match)
match2 = re.match(r'cat','dog cat dog')
print (match2)


# In[25]:

# What is the difference between re.match vs re.search


# In[26]:

# re.match("c","abcdef") # re.match() checks for a match only a the beginning of the string, while re.search() checks for 
# match anywhere in the string. 


# In[27]:

re.match("c","abcdef") # ^


# In[28]:

re.match("a","abcdef")


# In[29]:

re.search("c","abcdef")


# In[30]:

if 'c' in 'abcdef':
    print ('yes')


# In[31]:

contactInfo = 'Doe, John: 555-1212'


# In[32]:

re.search(r'\w+, \w+: \S+',contactInfo)


# In[33]:

match = re.search(r'(\w+), (\w+): (\S+)',contactInfo)


# In[34]:

match.group(1)


# In[35]:

match.group(2)


# In[36]:

match.group(3)


# In[37]:

match.group(0) # This will get printer without the paranthesis


# In[38]:

# Grouping by Name Using match.group


# In[39]:

match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)',contactInfo)


# In[40]:

contactInfo


# In[41]:

match


# In[42]:

match.group('last')


# In[43]:

match.group('first')


# In[44]:

match.group('phone')


# In[45]:

# findall

re.findall(r'(\w+), (\w+): (\S+)',contactInfo)


# In[46]:

ip = "192.168.254.1234"
res = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",ip)
print(res)


# In[52]:

ip = "192.168.254.12345 1hjhjhjhjhj"
res = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,5}\b",ip)
print(res)


# In[98]:

t = 'Showing 13 to 300 of 3000 (1 pages)'


# In[99]:

p = r"Showing ([0-9]+) to ([0-9]+) of ([0-9]+) \(([0-9]+) pages\)"


# In[102]:

re.findall(p,t)


# In[104]:

# How to get 3000
re.findall(p,t)[0][2]


# In[105]:

t = '10-5-2017'
p = r'(\d{1,2})-(\d{1,2})-(\d{4})'


# In[106]:

re.findall(p,t)


# In[107]:

# the other way 
p = r'(?P<mon>\d{1,2})-(?P<day>\d{1,2})-(?P<year>\d{4})'
re.findall(p,t)


# In[110]:

for m in re.finditer(p,t):
    print (m.group('mon'),m.group('year'),m.group('day'))


# In[111]:

# In order to avoid recompilatio every time, better compile it once
reo = re.compile(p)


# In[112]:

reo.findall(t)


# In[113]:

name_for_userid = {
    382: "raj",
    383: "Suman"
}


# In[118]:

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid,'None')


# In[119]:

greeting(382)


# In[53]:

txt = 'Oct 28 13:04:36  stm[4167]: <124004> <DBUG> |AP suman-hardening@1.2.3.5 stm|  status server processed for server radsec'
pattern = r'(?P<month>[a-zA-Z]{3}) (?P<date>[\d]{1,2}) (?P<timestamp>\b[\d:]+\b)  (?P<error>[\w]+\[[\d]+\]): (?P<msg>.+)'
reo = re.compile(pattern)
dct = {}
match = reo.search(txt)
if match:
    errorlist = dct.get(match.group('error'),None)
    if not errorlist:
        dct[match.group('error')] = [match.group('msg')]
    else:
        dct[match.group('error')].append(match.group('msg'))
for i in dct.keys():
    print (i,len(dct[i]))


# In[54]:

text = 'Oct 28 12:20:44  cli[4141]: <341004> <WARN> |AP suman-hardening@1.2.3.5 cli|  Set amp discover allowed: code: fail-prov-no-shipped.'
pattern = r'(?P<month>\b[a-zA-Z]{3}\b) (?P<date>\b[\d]{1,2}\b) (?P<timestamp>\b[\d:]+\b)  (?P<error>[a-zA-Z]+\[[\d]+\]:) (?P<msgtype>\<[\d]+\>) (?P<msg>.+)'
match = re.search(pattern,text)
match.group('msg')


# In[ ]:



