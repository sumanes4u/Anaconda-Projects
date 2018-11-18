
# coding: utf-8

# In[1]:

# Function/Method


# In[ ]:

planforweekends
- go for shopping # 1
 - go for camping # 2
 - go for fishing # 3


# In[8]:

# 1

def planforweekends():
    print ('go for Shopping')
    print ('go for camping')
    print ('go for fishing')


# In[5]:

planforweekends()


# In[9]:

#2
def planforweekends(act1,act2,act3):
    print ('go for ' + act1)
    print ('go for ' + act2)
    print ('go for ' + act3)


# In[7]:

planforweekends('Shopping','Camping','Fishing')


# In[10]:

planforweekends('Fishing','Camping','Shopping')


# In[14]:

planforweekends('Fishing','Camping')


# In[18]:

#3
def planforweekends(act1,act2,act3='Shopping'):
    print ('go for ' + act1) # statement1
    print ('go for ' + act2) # Statement2
    print ('go for ' + act3) # Statement3


# In[17]:

planforweekends('Fishing','Camping','Treeking')


# In[19]:

# Want to do a sum of two numbers


# In[30]:

#1
def sum(a,b):
    """ This function performs sum of two numbers"""
    c = a + b
    print ('Sum is : ', c)


# In[23]:

sum(7,3)


# In[27]:

help(sum)


# In[31]:

#2
def sum1(a,b):
    """ This function performs sum of two numbers"""
    c = a + b
    return c 


# In[32]:

sum1(7,3)


# In[33]:

x = sum1(10,15)


# In[34]:

x


# In[35]:

y = sum(10,15)


# In[36]:

y


# In[37]:

#3

def check_number(number):
    if number % 2 == 0:
        print (number, " is even")
    else:
        print (number," is odd ")


# In[38]:

check_number(10)


# In[39]:

check_number(7)


# In[41]:

#4 Multiple values from a function

def sum_subtract(a,b):
    c = a + b
    d = a - b
    return c,d


# In[43]:

x,y=sum_subtract(10,20)


# In[44]:

x


# In[45]:

y


# In[46]:

#5

def sum_add_sub_mul_div(a,b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c,d,e,f


# In[47]:

sum_add_sub_mul_div(10,15)


# In[56]:

p = sum_add_sub_mul_div(10,15)


# In[57]:

type(p)


# In[58]:

for i in p:
    print (i, end=', ')


# In[51]:

t = (1,2,3,4)


# In[52]:

for i in t:
    print (i)


# In[53]:

t


# In[59]:

# define function within another function


# In[68]:

#6
def display(str):
    def message():
        return 'Hi, Hello '
    result = message()+str
    return result


# In[64]:

display("Krishna")


# In[65]:

display("Ashir")


# In[67]:

# Functions are first class objects


# In[71]:

#7 

def out(input1):
    return 'Hey ' + input1

def message():
    return 'How are you? '


# In[72]:

out(message())


# In[78]:

#8

def out(input1):
    def message():
        return 'How are you?'
    return message()


# In[79]:

out(message())


# In[91]:

#9
def out(input1):
    def message():
        return 'How are you? ' + input1
    return message


# In[92]:

xyz = out('Hi')


# In[93]:

print(xyz())


# In[94]:

name = 'Raj'


# In[98]:

print (name)


# In[97]:

print(xyz())


# In[ ]:

# attribute vs function

asdfasd
asdfa()


# In[99]:

xyz = out(name)


# In[100]:

print(xyz())


# In[101]:

# Pass by object reference


# In[102]:

a = 10


# In[103]:

a


# In[104]:

id(a)


# In[105]:

b = 10


# In[106]:

id(b)


# In[107]:

print (a,id(a))


# In[109]:

def mod(a):
    a = 10
    print (a,id(a))


# In[111]:

a = 20
mod(a)
print (a,id(a))


# In[115]:

def modify(lst):
    lst.append(9)
    print (lst,id(list))


# In[113]:

lst = [1,2,3,4]


# In[116]:

modify(lst)


# In[117]:

print (lst,id(lst))


# In[118]:

# object is immutable = modified value is not available outside the function
# object is mutable = modified value is available. 


# In[119]:

# Functional programming


# In[1]:

import re
text = ''' show version
Aruba Operating System Software.
ArubaOS (MODEL: 225), Version 8.3.0.0
Website: http://www.arubanetworks.com
(c) Copyright 2017 Hewlett Packard Enterprise Development LP.
Compiled on 2017-11-12 at 09:42:46 PST (build 62262) by p4build
FIPS Mode :disabled

AP uptime is 19 hours 22 minutes 23 seconds
'''
pattern = r'((Version ([\d.]+)\n.*\n.*\n.*\(build ([\d]+)))'
#pattern = r'build ([\d]+)'
match = re.search(pattern,text)
print ('Version: '+match.group(3)+' Build: '+match.group(4))


# In[ ]:



