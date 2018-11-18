
# coding: utf-8

# In[1]:

# function

def sum1(a,b):
    c = a + b
    print (c)


# In[2]:

sum1(2,5)


# In[3]:

# Anonymous functions or Lambdas


# In[4]:

def square(x):
    return x*x


# In[6]:

square(3)


# In[13]:

y = lambda x: x*x # Anonymous function 


# In[14]:

value = y(5)


# In[15]:

value


# In[16]:

f = lambda x,y : x+y


# In[17]:

f(2,5)


# In[19]:

max = lambda x,y : x if x>y else y


# In[20]:

max(2,3)


# In[23]:

def compare(x,y):
    if x > y:
        print (x)
    else:
        print (y)


# In[24]:

compare(2,3)


# In[26]:

# filter
# filter(function,sequence)


# In[27]:

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# In[28]:

lst = [1,2,3,4]


# In[30]:

lst1 = list(filter(is_even,lst))


# In[31]:

lst1


# In[32]:

if True:
    print ('hi')


# In[33]:

name = 'Raj'


# In[34]:

name == 'Raj'


# In[35]:

if name == 'Raj':
    print ('hi')


# In[36]:

if name == 'Raj2':
    print ('hi')


# In[40]:

# 1 and 2
def odd_even(number):
    if number % 2 == 0:
        print ('The number is even')
    else:
        print ('The number is odd')


# In[39]:

odd_even(5)


# In[46]:

#1

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# In[49]:

#2
if is_even(4):
    print ("This is even")
else:
    print ("This is false")


# In[48]:

if is_even(3):
    print ("This is even")
else:
    print ("This is false")


# In[50]:

x = 6


# In[51]:

id(x)


# In[52]:

x = 7


# In[53]:

id(x)


# In[54]:

lst = [10,23,45,46,70,80]


# In[57]:

lst1 = list(filter(lambda x: (x%2 == 0),lst)) # compact
print (lst1)


# In[60]:

def sum1(a,b):
    """ This does the sum"""
    c = a + b
    print (c)


# In[63]:

sum.__doc__


# In[62]:

#del sum


# In[64]:

sum1(4,5)


# In[65]:

help(sum)


# In[66]:

numbers_list = [1,2,3,4]


# In[67]:

numbersSum = sum(numbers_list)


# In[68]:

numbersSum


# In[70]:

start = 2


# In[71]:

numbersSum = sum(numbers_list,2)


# In[72]:

numbersSum


# In[73]:

# map


# In[75]:

#map(function,sequence)


# In[76]:

# map(it acts) vs filter(return whatever it is processing)


# In[77]:

def squares(x):
    return x*x


# In[78]:

lst = [1,2,3,4,5]


# In[79]:

lst1 = list(map(squares,lst))
print (lst1)


# In[80]:

lst2 = list(map(lambda x : x*x, lst))
print (lst2)


# In[81]:

# map (lambda x,y: x*y, lst1,lst2)


# In[82]:

lst1=[1,2,3,4,5]


# In[83]:

lst2 = [10,20,30,40,50]


# In[84]:

lst3 = list(map(lambda x,y: x*y, lst1,lst2 ))


# In[85]:

lst3


# In[86]:

# reduce(function,sequence)


# In[87]:

lst


# In[91]:
from functools import reduce
reduce(lambda x,y: x*y, lst)


# In[90]:

from functools import reduce


# In[92]:

sum = reduce(lambda a,b: a+b, range(1,10))


# In[93]:

sum


# In[94]:

# lambda is just another form of function without name


# In[95]:

#map,filter,reduce they all need function.


# In[ ]:



