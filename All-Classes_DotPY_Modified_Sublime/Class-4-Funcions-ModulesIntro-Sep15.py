
# coding: utf-8

# In[1]:

# Functions (Methods) and Modules


# In[3]:

#1
cost1 = 35 # variable 
cost2 = 20 

def sumCart():
    cost1 = 45
    print (cost1)
    totalCost = cost1 + cost2
    print (totalCost)

sumCart()
print (cost1)


# In[5]:

dir('builtins')


# In[6]:

# Namespace 



# In[7]:

dir()


# In[9]:

# 2 . Arguments

cost1 = 15
cost2 = 20

def sumCart(item1,item2):
    totalCost = item1 + item2
    print (totalCost)
    
sumCart(cost1,cost2)


# In[2]:

sumCart(40,50)


# In[11]:

#3.

def sumCart(item1,item2=5):
    totalCost = item1 + item2
    print (totalCost)


# In[12]:

sumCart(5,2)


# In[13]:

sumCart(5)


# In[15]:

cost1


# In[16]:

cost2


# In[17]:

cost1=60


# In[18]:

def sumCart():
    totalCost = cost1 + cost2
    print (totalCost)


# In[19]:

sumCart()


# In[20]:

cost1=100


# In[21]:

sumCart()


# In[22]:

#4.

cost1=10
cost2=20
cost3=30
cost4=40

def sumCart(item1,item2):
    totalCost = item1 + item2
    return totalCost


# In[23]:

cart1 = sumCart(cost1,cost2)


# In[24]:

cart2 = sumCart(cost3,cost4)


# In[25]:

print (cart1)


# In[26]:

print (cart2)


# In[27]:

# Function - builtin


# In[28]:

#str()


# In[31]:

number = 10
print ('The number is ' + str(number))
type(number)


# In[30]:

type(number)


# In[32]:

number


# In[33]:

number1 = str(number)


# In[34]:

type(number1)


# In[35]:

x = int(input("please type your age "))
print (x)


# In[36]:

x = 10


# In[37]:

type(x)


# In[38]:

y = str(x)


# In[40]:

type(y)


# In[41]:

x = 'hi'


# In[42]:

#y = int(x)  --> ValueError: invalid literal for int() with base 10: 'hi'


# In[43]:

#int, float, str 


# In[44]:

x = 1.5


# In[45]:

y = int(x)


# In[46]:

y


# In[47]:

z = int(y)


# In[48]:

z


# In[49]:

a = float(y)


# In[50]:

a


# In[51]:

# int > float > str ( natural way )


# In[53]:

numbers = list(range(11))
print (numbers)


# In[54]:

# Modules


# In[55]:

dir()


# In[56]:

import finance


# In[57]:

dir()


# In[58]:

from finance import addTax


# In[59]:

dir()


# In[60]:

addTax(100,5)


# In[61]:

import os
os.getcwd()


# In[62]:

dir()


# In[63]:

import finance1


# In[64]:

#from finance1 import addTax1 ---> ImportError: cannot import name 'addTax1'


# In[65]:

dir()


# In[68]:

from finance1 import addTax


# In[67]:

del addTax


# In[69]:

dir()


# In[70]:

import random


# In[72]:

myList =[1,2,3,4,5]
print(random.choice(myList))


# In[73]:

import math


# In[74]:

import datetime


# In[75]:

import os


# In[77]:

import webbrowser


# In[79]:

#open webbrowser.open_new("https://nytimes.com")


# In[3]:

import webbrowser 


# In[4]:

webbrowser.open_new("http://nytimes.com")


# In[ ]:



