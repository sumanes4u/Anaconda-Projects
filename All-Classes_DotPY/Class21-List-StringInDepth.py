
# coding: utf-8

# In[2]:

# Single Quotes
print ('Hello World')

# Double Quotes
print ("Hello World")

# Triple quotes, preserve characters.
print ( """
 Hello
 World
 !
""" )


# In[3]:

a = 7


# In[4]:

type(a)


# In[5]:

a = 'Raj'


# In[6]:

type(a)


# In[7]:

a = '7' # unnecessary quote 


# In[8]:

type(a)


# In[9]:

a = '''Hello 
World'''


# In[10]:

a


# In[11]:

a = "Raj"


# In[12]:

a = "Raj went to scholl at 7 o'clock"


# In[13]:

# list 


# In[14]:

colors = ['red','blue','green',1,2,3,7.8]


# In[15]:

colors[3]


# In[16]:

# assignment


# In[17]:

colors[0] = 'magenta'


# In[18]:

colors


# In[19]:

another_list = [4,5,6]


# In[20]:

final_list = colors + another_list


# In[21]:

final_list


# In[22]:

# python list one of wonderful


# In[23]:

squares = [1,4,9,16]


# In[24]:

sum = 0
for num in squares:
    sum += num 
print (sum)


# In[25]:

list = ['Smith','John','Donald']

if 'John' in list:
    print ('Yes')


# In[26]:

a = [1,2,3,4,5,6,7,8]


# In[27]:

# while

i = 0
while i < len(a):
    print (a[i])
    i = i + 3


# In[28]:

# List Methods


# In[29]:

list.append
list.insert
list.extend
list.index
list.remove
list.sort
list.reverst
list.pop


# In[30]:

list = ['Raj','John','Smith']


# In[31]:

list.append('Donald')


# In[32]:

list


# In[33]:

list.insert(0,'Harry')


# In[34]:

list


# In[35]:

list.extend(['abc','xyz'])


# In[36]:

list


# In[37]:

list.index('John')


# In[38]:

list.remove('Smith')


# In[39]:

list


# In[40]:

list.pop()


# In[41]:

list.pop()


# In[42]:

rejected_candidates = list.pop()


# In[43]:

rejected_candidates


# In[44]:

list


# In[45]:

rejected_candidates


# In[46]:

# list slices


# In[47]:

list = ['a','b','c','d']


# In[48]:

alist = list[2:4]


# In[49]:

alist


# In[50]:

list


# In[51]:

list[0]='y'


# In[52]:

list


# In[53]:

list[0:4]='z'


# In[54]:

list.


# In[55]:

# sorting


# In[56]:

# difference between list sort method and the builtin sorted. 
# difference between append and extend
a = [5, 1, 4, 3]
print ( sorted(a) ) ## [1, 3, 4, 5]
print ( a )  ## [5, 1, 4, 3]

strs = ['aa', 'BB', 'zz', 'CC']
print ( sorted(strs) )  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print ( sorted(strs, reverse=True) )   ## ['zz', 'aa', 'CC', 'BB']

strs = ['ccc', 'aaaa', 'd', 'bb']
print ( sorted(strs, key=len) )  ## ['d', 'bb', 'ccc', 'aaaa']

## "key" argument specifying str.lower function to use for sorting
print ( sorted(strs, key=str.lower) )  ## ['aa', 'BB', 'CC', 'zz']

## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd', 'wa']


## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
    return s[-1]


## Now pass key=MyFn to sorted() to sort by the last letter:
print ( sorted(strs, key=MyFn) )  ## ['wa', 'zb', 'xc', 'yd']


# In[57]:

list = [4,3,2,1]


# In[58]:

list.sort()


# In[59]:

list


# In[60]:

a = [5, 1, 4, 3]
print ( sorted(a) ) ## [1, 3, 4, 5]
print ( a )  ## [5, 1, 4, 3]


# In[61]:

strs = ['aa', 'BB', 'zz', 'CC']
print ( sorted(strs) )  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print ( sorted(strs, reverse=True) )   ## ['zz', 'aa', 'CC', 'BB']


# In[62]:

strs = ['ccc', 'aaaa', 'd', 'bb']
print ( sorted(strs, key=len) )  ## ['d', 'bb', 'ccc', 'aaaa']


# In[63]:

strs = ['ccc', 'aaaa', 'd', 'bb']
print ( sorted(strs, key=len, reverse=True) )  ## ['d', 'bb', 'ccc', 'aaaa']


# In[64]:

l = [1,5,4,3]


# In[65]:

l.sort()


# In[66]:

l


# In[67]:

l2 = [9,4,5,6]


# In[68]:

sorted(l2)


# In[69]:

l2


# In[70]:

print ( sorted(strs, key=str.lower) )


# In[82]:

strs


# In[83]:

strs = ['aa', 'BB', 'zz', 'CC']


# In[1]:

sorted(strs, key=str.lower) # case insensitive


# In[85]:

sorted(strs)


# In[86]:

strs = ['xc', 'zb', 'yd', 'wa']


# In[87]:

def MyFn(s):
    return s[-1]


# In[88]:

l3 = [1,2,3,4]


# In[89]:

l3[-1]


# In[91]:

MyFn(strs)


# In[92]:

sorted(strs, key=MyFn)


# In[93]:

def MyFn2(s):
    return s[0]


# In[94]:

sorted(strs, key=MyFn)


# In[95]:

# Python Import

import math
print(math.pi)

from math import pi
print ( pi )

import sys

print ( sys.path )


# In[96]:

import re


# In[99]:

list = range(10)


# In[101]:

list = [0,1,2,3,4,5,6,7,8,9]


# In[102]:

import time


# In[103]:

time.time()


# In[104]:

import timeit


# In[106]:

timeit.time(MyFn(s))


# In[107]:

s = 'abc'


# In[111]:

timeit.timeit(MyFn(s))


# In[112]:

lst = [1,2,3,4,5]


# In[113]:

def costly_func(lst):
    return map(lambda x: x^2, lst)


# In[115]:

str = 'Today is my lucky day'

print (str)          # Prints complete string
print (str[0] )      # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])
print (str[:7]  )    # Prints string starting from 3rd character
print (str * 2 )     # Prints string two times
print (str + "TEST") # Prints concatenated string
print (str[0:5:2])


# In[116]:

print (lst[0])


# In[117]:

lst = ['abc','def','xyz']


# In[118]:

print (lst[0])


# In[119]:

str = 'abc'


# In[120]:

str[0]


# In[121]:

str = 'Today is my lucky day'


# In[122]:

str[2:5]


# In[123]:

str[2:]


# In[124]:

str[:5]


# In[125]:

str[0:5:2] # start : 0 , end = 5, step = 2


# In[126]:

str[0:5:1] # start : 0 , end = 5, step = 1


# In[135]:

a = 'a,b,c,d,a,a'


# In[131]:

a.split(',')


# In[132]:

# string methods vs list methods


# In[136]:

a.count('a')


# In[ ]:



