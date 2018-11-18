
# coding: utf-8

# In[6]:

# Regex - regular expression. 
import re
p = 'this' # match this 
s = 'this does not contain text this' # from this. 
#1
m = re.search(p,s)
print (m)

#2
print (m.start())
print (m.end())

#3
m1 = re.findall(p,s)
print(m1)

#4.
# # get matched object, which gives more information.
for m in re.finditer(p,s):
    print ("found at", m.start(), m.end())


# In[7]:

pattern = 'xy'
string = 'xxyyxyxyxyxy'
#1
result = re.search(pattern,string)
print(result.start())
print(result.end())

#2
m2 = re.findall(pattern,string)

print(m2)

#3
for m in re.finditer(pattern,string):
    print ("found at", m.start())


# In[8]:

# pattern matches never overlaps.

p = 'sas'
t = 'sasasas'

print (re.findall(p,t))


# In[10]:

# search are always greedy.

p = 'ab*' # * means it will match zero or more occurence. (a)
t = 'abbbababbbbbbbbabababa'

print (re.findall(p,t))


# In[11]:

p = 'ab+' # + means it will match atlease one occcurence
t = 'abbbababbbbbbbbabababa'

print (re.findall(p,t))


# In[12]:

p = 'ab?' # question represt,optional and only character. 
t = 'abbbababbbbbbbbabababa'

print (re.findall(p,t))


# In[18]:

p = 'ab{3}' # 3 repeatation of b. 
t = 'abbbababbbbbbbbabababa'

print (re.findall(p,t))


# In[20]:

p = 'ab{2,5}'
t = 'abbbababbbbbbbbabababa'
print (re.findall(p,t))


# In[26]:

p = '((ma){2})'
s = 'mama'
print (re.findall(p,s))


# In[30]:

p = 'a[ab]+'
t = 'abbbababbbbbbbbabababa'

print (re.findall(p,t))


# In[28]:

p = 'a[ab]+'
t = 'abbbababbbbsbbbbabababaaaa'

print (re.findall(p,t))


# In[33]:

p = 'a[ab]+?' # makes + works in non-greedy way. 0/1
t = 'abbbababbbbsbbbbabababaaaa'

print (re.findall(p,t))


# In[35]:

t = 'http://www.google.com'
p = 'http'

print (re.findall(p,t))


# In[37]:

t = '://www.google.com'
p = 'http'

print (re.findall(p,t))


# In[38]:

p = '^http' # ^ stands for starting 
t = 'http://www.google.com'
print (re.findall(p,t))


# In[39]:

t = 'http://www.google.com'
p = 'com$' # $ stands for ending 
print (re.findall(p,t))


# In[43]:

t = 'He is a superman of He'
p = 'He$'
m = re.search(p,t)
print (m)


# In[44]:

p = 'a(ab)*'
t = 'abbbababbbbsbbbbabababaaaabababab'
print (re.findall(p,t))


# In[53]:

import re
p = 'a(ab)*'
t = 'aab'
print (re.findall(p,t))


# In[54]:

p = '^[a-z0-9_-]{3,16}$'

t = 'om'

print (re.findall(p,t))


# In[59]:

p = '^[a-z0-9_-]{3,16}$'

t = 'omioim_-'

print (re.findall(p,t))


# In[60]:

p = '^[a-z0-9_-]{3,16}$'

t = 'omi+'

print (re.findall(p,t))


# In[14]:

t = 'oidasddaASFG_a-1'
p = '^[a-z0-9_-]{3,16}$'

#print (re.findall(p,t))
print (re.findall(p,t,re.IGNORECASE))


# In[67]:

re.findall('test', 'TeSt', re.IGNORECASE)


# In[4]:

import re
t = 'man eats mango'

p = '((man)(go))'

print (re.findall(p,t))

for m in re.finditer(p,t):
    print (m.group()) # group. 
    #print (m)  


# In[ ]:



