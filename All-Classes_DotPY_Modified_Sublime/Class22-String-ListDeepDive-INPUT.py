
# coding: utf-8

# In[1]:

str = 'Today is my lucky day'

print (str)          # Prints complete string
print (str[0] )      # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])
print (str[:7]  )    # Prints string starting from 3rd character
print (str * 2 )     # Prints string two times
print (str + "TEST") # Prints concatenated string
print (str[0:5:2])

print ('====== 2 ========')


print (str[::-1])

#print str[-1]


#print str[5:2:-1];print str[::-1];
str[-3]
print (str[-1:-5:-1])

str="HelloPython"
# 1 2 3 4 5 6 7 8 9 10 11
# H e l l 0 P y t h o n

# String Slices


print (str[1:5:2]) #begin,end,step
print (str[5:])
print (str[-5])  #from last
print (str[15:])  #no output ; no exception is thrown like in C, C++ etc.
print (str[:])

#reverse string
print (str[-1::-1])
print (str[::-1])

print (str[-2:-5:-1])


#Tuple
str2=(1,2,3,"hello",True,None,7,8,9,0,5,4) #heterogenious array
print (str2[::-1])

data=(1,2,3,4,5)
data = (100,200)  #overwrites


# In[2]:

a = "Hello"


# In[3]:

print(a[::-1])


# In[4]:

str="HelloPython"


# In[5]:

print (str[4:]) 


# In[6]:

print (str[15:]) 


# In[7]:

l = [1,2,3,4]


# In[8]:

print(l[0])


# In[11]:

print(l[15:])


# In[12]:

# immutable


# In[13]:

l = [1,2,3,4]


# In[14]:

t = (1,2,3,4)


# In[15]:

l[0] = 5


# In[16]:

print(l)


# In[17]:

##t[0] = 5 # you want to put some restriction. - TypeError: 'tuple' object does not support item assignment


# In[18]:

# Slicing [2:5:2] - string, list, tuple


# In[19]:

data=(1,2,3,4,5)
data = (100,200)  #overwrites


# In[20]:

print(data)


# In[21]:

l = [1,2,3,4]


# In[22]:

l = [5,6]


# In[23]:

print(l)


# In[24]:

s = 'United States of America'

print ( s.lower(), s.upper() ) # -- returns the lowercase or uppercase version of the string
print ( s.strip() ) # -- returns a string with whitespace removed from the start and end
print ( s.isalpha() )
print ( s.isdigit() )
print ( s.isspace() ) # ... -- tests if all the string chars are in the various character classes
print ( s.startswith('other') )
print ( s.endswith('other') ) # -- tests if the string starts or ends with the given other string
print ( s.find('other') ) # -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
print ( s.replace('old', 'new') ) # -- returns a string where all occurrences of 'old' have been replaced by 'new'
print ( s.split('delim') ) # -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
#print ( s.join(list) ) # -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc


# In[29]:

s = 'United States of America'
p = 'United,States,America'


# In[26]:

print(s.lower())


# In[27]:

print(s.upper())


# In[28]:

print(s.strip())


# In[33]:

print(p.strip(",").split(","))


# In[32]:

print(p.split(","))


# In[40]:

# diff string vs list
# We cannot modify string


# In[35]:

print(s[0])


# In[36]:

l = [1,2,3,4]


# In[37]:

l[0] = 5


# In[38]:

print(l)


# In[39]:

#s[0]=5 --- TypeError: 'str' object does not support item assignment


# In[41]:

m = ' Hello '


# In[42]:

print(m.strip())


# In[43]:

m = ',Hello,'


# In[44]:

print(m.strip(","))


# In[45]:

m = 'United,States,of,america,'


# In[46]:

print(m.strip(","))


# In[47]:

print(m.split(","))


# In[52]:

print(m.strip(",").split(","))


# In[54]:

p = ' United,States,of,america'


# In[56]:

print(p.strip().split(",")) # It is always safe to strip option, so that it removes unwanted characters from start/end.


# In[57]:

q = p.strip().split(",")


# In[58]:

print(q)


# In[68]:

str1 = ' '.join(q) # convert from list to string


# In[69]:

print(str1)


# In[70]:

print(q[0])


# In[71]:

print(str1[0])


# In[74]:

list1 = ['1','2','3']


# In[75]:

str2 = "".join(list1)


# In[76]:

print(str2)


# In[79]:

list1 = ['1','2','3']


# In[80]:

str1=''.join(list1)


# In[81]:

list1 = [1,2,3]

print(str1)
# In[83]:

#str1 = ''.join([str(e) for e in list1])  --- works in jupyter notebook


# In[84]:

# list comprehension


# In[85]:

list12 = [1,2,3,4]


# In[90]:

for e in list12: # multi-liner
    print (e**2)


# In[91]:

[x**2 for x in list12] # one liner


# In[92]:

S = [x**2 for x in range(10)]


# In[93]:

print(S)


# In[94]:

M = [x for x in S if x % 2 == 0]


# In[95]:

print(M)


# In[96]:

oddlist = []
evenlist = []

for i in list12:
    if i%2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print (oddlist)
print (evenlist)


# In[100]:

print(2 != 2)


# In[99]:

#2 ne 3


# In[101]:

oddlist = []
evenlist = []

for i in list12:
    if i%2 != 0:
        oddlist.append(i)
    else:
        evenlist.append(i)
print (oddlist)
print (evenlist)


# In[108]:

s = 'United States of America'

print ( s.isspace() ) # ... -- tests if all the string chars are in the various character classes
print ( s.startswith('United') )
print ( s.endswith('other') ) # -- tests if the string starts or ends with the given other string
print ( s.find('United') ) # -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
print ( s.replace('America', 'Emirate') ) # -- returns a string where all occurrences of 'old' have been replaced by 'new'
print ( s.split(' ') ) # 


# In[112]:

# You can timeit as well.

a = '0123456789'

def reverse(input):
    n = len(input)
    x=""
    for i in range(n-1,-1,-1):
        x += input[i]
    return x

print ( reverse('12345') )

import timeit

print ( timeit.timeit((a[::-1])))  # lesser time
print ( timeit.timeit(reverse('123456789')) ) # lesser time.


# In[113]:

print(list(range(0,10)))


# In[118]:

sum1 = 0
x = ''
for i in range(0,10,2):
     sum1 += i
#     return x


# In[119]:

l = [1,2,3,4,5]
sum = 0
for i in l:
    sum += i
print (sum)


# In[ ]:



