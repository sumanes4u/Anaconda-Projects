
# coding: utf-8

# In[44]:

# Arrays - similar list but in this you can only store one type data. 
# numpy


# In[ ]:

#type code    size

#'b' - signed integer - 1 
#'B' - unsigned integer - 1
#'i' - signed integer - 2 
#'I' - unsigned integer - 2
#'l' - signed integer - 4
#'L' - unsigned integer - 4
#'f' - floating point - 4
#'d' - double precision floating point - 8
#'u' - unicode character  - 2


# In[2]:

# arrayname = array(type code,[elements])


# In[ ]:
from array import *
tuple1 = (1,2,3,4)
arrayname = array('i',[1,2,3,4])


# In[46]:

list = [1,'a',20,'hi']


# In[5]:

from array import *
a = array('i',[4,6,2,9]) # type of integer array


# In[6]:

a


# In[13]:

# float type array, f , d = double precision floating point

arr = array('d',[1.5,-2.2,3,5.75])


# In[8]:

arr


# In[9]:

# printing an array


# In[45]:

for el in a:
    print (el)


# In[12]:

for element in arr:
    print (element)


# In[14]:

# character array

from array import *
arr = array('u',['a','b','c','d','e'])

print ('The array element are : ')
for ch in arr:
    print (ch)


# In[25]:

# creating array from another array
from array import *

arr3 = array('d',[1.5,2.5,-3.5,4])

arr4 = array(arr3.typecode,(a*3 for a in arr3))

for i in arr4:
    print (i)


# In[26]:

# Indexing and Slicing on Arrays


# In[ ]:

#10 20 30 40 50
#0   1  2  3  4


# In[27]:

# ex 

from array import *
x = array('i', [10,20,30,40,50]) # type integer

n = len(x)

for i in range(n):
    print (x[i], end=' ')


# In[28]:

# 

from array import *
x = array('i', [10,20,30,40,50])

n = len(x)

i = 0
while i < n:
    print (x[i], end = ' ')
    i += 1


# In[30]:

y = x[1:4]
print (y)

y = x[0:]
print (y)

y = x[:4]
print (y)


# In[32]:

# ex 

from array import *
x = array('i',[10,20,30,40,50,60,70])

for i in x[2:5]: # slicing a portion of the array 
    print (i)


# In[ ]:




# In[33]:

# processing the arrays 


# In[36]:

# ex

from array import *

arr = array('i',[10,20,30,40,50])
print ('orig array: ', arr)

arr.append(60)
arr.append(70)

print ('modified array: ', arr)

arr.insert(1,99)
print ('modified array: ', arr)

arr.remove(20)
print ('modified array: ', arr)

n = arr.pop()
print ('modified array: ', arr)

# convert an array into a list using tolist()
lst = arr.tolist()
print ('List: ', lst)
print ('Array: ', arr)


# In[1]:

# ex 

#from array import *
str = input('Enter marks: ').split(' ')

marks = [ int(num) for num in str] 
type(marks)

sum = 0 
for x in marks:
    print (x)
    sum += x
print ('Total marks: ', sum)

n = len(marks)
percent = sum/n
print ('Percentage: ', percent)


# In[52]:

# sorting an array using Bubble sort technique

x = array('i',[]) # empty list

print ('How many elements: ', end='')
n = int(input()) # getting a user input

for i in range(n): # how many elements
    print ('Enter element: ', end='')
    x.append(int(input())) # populating array
    
print ('Original array: ', x)

# bubble sorting 
flag = False # when the swapping is done, flag becomes True
for i in range(n-1): # i is from 0 to n-1
    for j in range(n-1-i): # j is from 0 to one element lesser than i
        if x[j] > x[j+1]: # if 1st element is bigger than the 2nd one
            t = x[j] # swap j and j+1 elements
            x[j] = x[j+1]
            x[j+1] = t
            flag = True # swapping done, hence flag is True. 
    if flag == False: # no swapping is done, array is in sorted order
            break # come out of loop. 
    else:
        flag = False # assing initial value to flag. 
print ('Sorted array= ', x)


# In[56]:

# ex
from array import *

x = array('i', [])

print ('How many elements? ', end='')
n = int(input()) 

for i in range(n):
    print ('Enter element: ', end='')
    #x.append(int(input())) # add the element to the array x 
    x.append(int(input()))
    
print ('Original array: ', x)

s = int(input()) # searching an element

flag = False

for i in range(len(x)):
    if s == x[i]:
        print ('Found at Position= ', i+1)
        flag = True
    if flag == False:
        print ('Not found in the array')


# In[ ]:

# Types of Arrays

#- Single Dimensional arrays
#- Multi-Dimensional array 


# In[58]:

marks = array('i',[50,60,70,80])


# In[1]:

marks = array([50,60,70,80], # first student
             [40,70,70,80], # second student
             [30,60,70,80]) # third student


# In[59]:

# numpy 


# In[60]:

import numpy
arr = numpy.array([10,20,30,40,50])
print (arr)


# In[61]:

import numpy as np
arr = np.array([10,20,30,40,50])
print (arr)


# In[62]:

# functions
# array()
# linspace()
# logspace()
# arange()
# zeros() and ones() functions


# In[ ]:



