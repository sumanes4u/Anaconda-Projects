
# coding: utf-8

# In[1]:

# Python Execution Model 


# In[2]:

number = 4 # number is a name


# In[3]:

number


# In[7]:

dir(__builtins__)


# In[8]:

dir()


# In[9]:

del number


# In[10]:

dir()


# In[11]:

address = "111, Baler Streee, NW London"


# In[12]:

dir()


# In[13]:

employee_details = {
    'name' : 'John',
    'role' : 'CEO',
    'SSN' : '12345'
}


# In[14]:

dir()


# In[15]:

# namespace 

# Everything in python is an object


# In[16]:

a = 5
dir(a)


# In[17]:

a = 5


# In[18]:

type(a)


# In[19]:

a


# In[20]:

# __ double underscore # dunder # magic methods 


# In[22]:

# __init__ or __str__ # magic methods or dunder init dunder. double score


# In[23]:

# search book


# In[24]:

# module ( package )


# In[25]:

import math # import a package


# In[27]:

math.cos(7)


# In[28]:

#from library.second_floor.section_x.row_three import book

# from library.second_floor.section_x.row_four import book


# In[29]:

# scope


# In[30]:

# Local versus Global 


# In[31]:

# creating a function


# In[37]:

cost1 = 20
cost2 = 30


# In[33]:

totalcost = cost1 + cost2


# In[34]:

totalcost


# In[35]:

def sumCart():
    totalCost = cost1 + cost2
    print (totalCost)


# In[38]:

sumCart()


# In[39]:

def sumCart(c1,c2):
    totalCost = c1 + c2
    print (totalCost)


# In[40]:

sumCart(7,10)


# In[47]:

def sumCart(c1,c2=10):
    totalCost = c1 + c2
    print (totalCost)


# In[42]:

sumCart(15)


# In[44]:

sumCart(10,50)


# In[48]:

sumCart(15)


# In[53]:

#1
def local():
    m = 7
    print (m)

m = 5
print (m)

local()


# In[56]:

#2
def local():
    # m is not found within the local scope, so it turns to final the global scope
    print (m,'print from the global scope')
    
m = 5
print (m,'print from the global scope - outside')

local()


# In[59]:

#3

def func():
    p = 3
    p = 4 # overwrite the previous one
    def local():
        print (p,'print it from the local scope')

    local()
p = 5
print (p)

func()


# In[63]:

#4

def func():
    global p  # specifically categorizing 
    p = 3
    def local():
        print (p,'print it from the local scope')

    local()
p = 5
print (p)

func()
print (p)


# In[ ]:



