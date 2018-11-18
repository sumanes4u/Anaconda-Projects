
# coding: utf-8

# In[4]:

#1 . 

import re

patterns = ['term1','term2']

text = 'This is a string with term1, but it does not have the other term'

for pattern in patterns:
    print ('Searching for "%s" in" \n"%s"' % (pattern,text),)
    
    if re.search(pattern, text):
        print ('\n')
        print ('Match was found \n')
        
    else:
        print ('No match was found')


# In[5]:

#2.

pattern = 'term1'

match = re.search(pattern,text)

print(type(match))


# In[6]:

print(match.start())


# In[7]:

print(match.end())


# In[8]:

# This match object returned by the search() method is more than just a boolean or No, it contains 
# information about the match, including the original input string, the regular expression that 
# used , and the location of the match. 


# In[12]:

print(match.re.pattern)


# In[22]:

print(match.string.capitalize())


# In[23]:

#3.

split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

print(re.split(split_term,phrase))


# In[27]:

# 4

# Finding all instances of a pattern

print(re.findall('match','test phrase match is in middle match'))


# In[28]:

print(re.finditer('match','test phrase match is in middle match'))


# In[18]:

#5. 

def multi_re_find(pattern,phrase):
    
    for pattern in patterns:
        print ('Searching the phrase using the re check: %r' %pattern)
        print (re.findall(pattern,phrase))
        print ('\n')


# In[19]:

print(multi_re_find('match',"This is the pattern match"))


# In[31]:

print(phrase)


# In[35]:

patterns = ['hello','domain']


# In[38]:

print(multi_re_find(patterns,phrase))


# In[47]:

#5.

phrase = 'sdsd..sssddd...sdddsddd...dsds..dssss...sdddd..sdd'

patterns = ['sd*','sd+','sd?','sd{3}','sd{2,3}',]


# In[48]:

#multi_re_find(test_patterns,test_phrase)  --> syntax


# In[50]:

phrase  = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'


# In[51]:

patterns = ['[sd]','s[sd]+']


# In[52]:

print(multi_re_find(patterns,phrase))


# In[54]:

#7. Exclusion

phrase = 'This is a string! But it has punctuation?. How can we remove it'

print(re.findall('[^!.? ]+',phrase))


# In[55]:

#8.

phrase = 'This is a an example sentence.Lets see if we can find some letters'

patterns = ['[a-z]+','[A-Z]+','[a-zA-Z]+','[A-Z][a-z]+']


# In[56]:

print(multi_re_find(patterns,phrase))


# In[57]:

# Escape Codes
# You can use special escape codes to find specific types of patterns in your data, such as digits
# , non-digits, whitespace and more

# \ Unfortunately, a backslash must itself be escaped in normal phtyhon strings. and that would
# results in expressions that are difficult to read. 


# In[64]:

phrase = "This is a string with some numbers 1233 and a symbol #hastag"

patterns = [r'\d+',r'\D+',r'\s+',r'\w+'] # readability purpose 


# In[65]:

print(multi_re_find(patterns,phrase))


# In[ ]:



