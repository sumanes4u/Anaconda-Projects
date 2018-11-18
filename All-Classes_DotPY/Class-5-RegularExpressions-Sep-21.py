
# coding: utf-8

# In[3]:

import re


# In[4]:

match = re.search('at','called baat')
match.group()


# In[5]:

match.group()


# In[6]:

def Find(pat,text):
    match = re.finditer(pat,text)
    if match:print (match)
    else: print ('not found')


# In[7]:

Find('xy','called baat xyt')


# In[8]:

Fin


# In[9]:

Find('..t','called baat xyt')


# In[10]:

def found(pat,text):
    matchy = re.search(pat,text)
    if matchy: 
        print (matchy.group())
    else: 
        print('not found')


# In[11]:

found(r'c.lled','baat called c.lled another term xyzt')


# In[36]:

import re

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print ('Looking for "%s" in "%s" ->' % (pattern, text),)

    if re.search(pattern,  text):
        print ('found a match!')
    else:
        print ('no match')


# In[39]:

import re

pattern = 'this'
text = 'Does this text this match this the this pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print ('Found "%s" in "%s" from %d to %d ("%s")'%(match.re.pattern, match.string, s, e, text[s:e]),)


# In[41]:

import re

text = 'abbaaabbbbaaaaab'

pattern='ab'

occur= len(re.findall(pattern , text))

e=0

while(occur>0):
 match = re.search(pattern,text[e:] )

 s = match.start() 
 e = match.end()
 print("occurence at (%d--%d)"%(s+e,e+e))
 occur-=1
""""
for match in re.findall(pattern, text):
    print 'Found at "[%s,%s]"' %(match.start ,match.end)
"""


# In[45]:

import re

text = 'abbbbnnnnnnnnbababannnnnnnnnnnaaababbbnnnnnnnbbannnnnnbbbbbabababannnnbababbbbbb'

pattern = 'an+'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print ('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[46]:

import re

text = 'abbbbnnnnnnnnbababannnnnnnnnnnaaababbbnnnnnnnbbannnnnnbbbbbabababannnnbababbbbbb'

pattern = 'an+'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print ('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[ ]:



