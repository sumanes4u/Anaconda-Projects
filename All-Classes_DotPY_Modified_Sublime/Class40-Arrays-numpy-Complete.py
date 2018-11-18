
# coding: utf-8

# In[44]:

# Arrays - similar list but in this you can only store one type data. 
# numpy


# In[ ]:

#type code    size#

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

from array import * # array package 
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


# In[50]:

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


# In[2]:

from array import *
marks = array('i',[50,60,70,80])


# In[4]:

marks = array([[50,60,70,80], # first student
             [40,70,70,80], # second student
             [30,60,70,80]]) # third student


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


# In[63]:

# Creating arrays using array()


# In[67]:

from numpy import * # import the package
arr = array(['a','b','c','d','e'])
print (arr)


# In[69]:

from numpy import *
arr = array(['Delhi','Indore'],dtype=str)
print (arr)


# In[70]:

# ex copy array

from numpy import *
a = array([1,2,3,4,5])

b = array(a) # creating b from a using array() function

c = a

print (a)
print (b)
print (c)


# In[72]:

# creating arrays linspace


# In[73]:

# a = linspace(0,10,5)


# In[105]:

from numpy import *

a = linspace(0,10,5) # drivide 0 to 10 into 5 parts
print (a)


# In[75]:

# logspace - similart to linspace

# logspace(start,stop,n)


# In[77]:

from numpy import *

a = logspace(1,5,5) # divide 1 power 10 to 4 power 10 into 5 equal parts

n = len(a)

for i in range(n):
    print ('%.1f' % a[i], end=' ')


# In[81]:

# ex 

from numpy import *
a = arange(2,11,2) # arange(start,stop,stepsize)
print (a)


# In[82]:

# creating arrays using zeros() and ones() function


# In[83]:

# zeroes(n,datatype)
# ones(n,datatype)


# In[107]:

from numpy import *
a = zeros(6,int)
print (a)

b = ones(7,int)
print (b)


# In[86]:

# Mathematical operation on Array


# In[87]:

# arr = array([10,20,30])
# arr = arr + 5 


# In[108]:

from numpy import *

arr = array([10,20,30])

print (arr)

print ('adding 5', arr + 5)

print (arr)


# In[91]:

print ('substracting 5', arr - 5)


# In[92]:

print ('multiply 5', arr * 5)


# In[93]:

print ("Sin Values", sin(arr))


# In[94]:

# Compare arrays


# In[98]:

a = array([1,2,3,0])
b = array([0,2,3,2])

c = a == b
print (c) # 1
c = a > b
print (c) # 2
c = a < b
print (c) # 3


# In[100]:

# any()

a = array([1,2,3,0])
b = array([0,2,3,2])

c = a > b
print (c)

# check if any one element is true

print (any(c))

# check if all elements are true

print (all(c))

if (any(a > b)):
   print ('a contains atleast one element greater than those of b')


# In[109]:

# logical operations

from numpy import *

a = array([1,2,3],int)
b = array([0,2,3],int)

c = logical_and(a> 0 , a < 1)
print (c)

c = logical_or(b >= 0 , b ==1)
print (c)

#false, true, true > not function > true, false, false
c = logical_not(b)
print (c)


# In[110]:

import numpy as np


# In[111]:

help(np.logical_not)


# In[115]:

# ex very important function of numpy

from numpy import *
a = array([10,20,30,40],int)
b = array([1,21,3,40],int)

# if a > b then take element from a else from b

c = where(a>b,a,b)
print (c)


# In[117]:

# ex very important function of numpy

from numpy import *
a = array([10,20,30,40],int)
b = array([1,21,3,40],int)

# if a > b then take element from a else from b

c = where(a>b,b,a) # inverse
print (c)


# In[118]:

# ex 
from numpy import *
a = array([1,2,0,-1,0,6],int)

# retrieve indexes of non zero elements from a
c = nonzero(a)

for i in c:
    print (i)
    
# display the element
print (a[c])


# In[ ]:

# aliasing the arrays
# a = b # This does not make any new copy of the array 'a'. 
from numpy import *
a = array([1,2,3])

b = a


# In[119]:

# ex

from numpy import *

a = arange(1,6)
b = a # shallow copy 

print ('orig array', a)
print ('Alias array', b)


b[0] = 50

print ('After modification')
print ('orig array', a)
print ('Alias array', b)


# In[120]:

# ex - copying 

from numpy import *

a = arange(1,6)

b = a.view() # creates a view of a and call it b
# viewing is similar to copying only, it is called as 'shallow copying" . "deep copying"

print ('orig array', a)
print ('View array', b)

b[0] = 50

print ('After modification')
print ('orig array', a)
print ('Alias array', b)


# In[122]:

# ex - copying 

from numpy import *

a = arange(1,6)

b = a.copy() # "deep copying" (copy()), shallow will (view()) effect the orig array. 

print ('orig array', a)
print ('View array', b)

b[0] = 50

print ('After modification')
print ('orig array', a)
print ('New array', b)


# In[123]:

# Slicing and Indexing in numpy Arrays


# In[124]:

from numpy import *

a = arange(10,16)
print (a)

b = a[1:6:2]
print (b)


# In[125]:

# Dimensions of Arrays


# In[127]:

# 1 row
arr1 = array([1,2,3,4,5])
print (arr1)

# 1 colum

arr2 = array([10,
             20,
             30,
             40])
print (arr2)


# In[132]:

# 2D
from numpy import *
arr5 = numpy.array([[1,2,3],
            [4,5,6]])
print (arr5)


# In[148]:

# 2D array as a combination of serveral 1D arrays.
from numpy import *
arr5 = numpy.array([[[1,2,3],[1,0,1]],
            [[4,5,6],[1,0,1]]])
print (arr5)
print (arr5.ndim)


# In[139]:

# attributes of an array


# In[140]:

# Numpy array class is called as ndarray. ie array. class ndarray or array
# ndim = represents the number of dimensions , ie rank , axes. 


# In[141]:

dir()


# In[142]:

help(array)


# In[155]:

arr1 = array([1,2,3,4]) # 1D array
print (arr1.ndim)
print (arr1.shape)
print (arr1.size)
print (arr1.itemsize)
print (arr1.dtype)
print (arr1.nbytes)


# In[152]:

arr2 = array([[1,2,3],
              [4,5,6]]) # 2D array
print (arr2.ndim)
print (arr2.shape)
print (arr2.size)


# In[156]:

# reshape

arr1 = arange(10)
print (arr1)


# In[157]:

arr1 = arr1.reshape(2,5)
print (arr1)


# In[158]:

arr1 = arr1.reshape(5,2)
print (arr1)


# In[161]:

# flatten()

arr2 = array([[1,2,3],
              [4,5,6]]) # 2D array

print (arr2)

arr2 = arr2.flatten()
print (arr2) # gets converted to 1D


# In[162]:

# ex 

a = array([1,2,3,4])
a = array([[1,2,3,4],[1,2,3,4]])


# In[163]:

# ones and zeros()


# In[165]:

# ones((rows,colums),dtype)

a = ones((3,4),float)
print (a)


# In[167]:

a = zeros((3,4),int)
print (a)


# In[168]:

# eye()

a = eye(3)
print (a)


# In[169]:

# Indexing in Multi-Dimensional arrays


# In[ ]:

a[0][0] # 0th rows and 0th column.
b[1][3] # 1st rows and 3rd column. 


# In[172]:

# ex 

a = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(a)):
    print ('first', a[i])
    
# display element by element

for i in range(len(a)):
    for j in range(len(a[i])):
        print (a[i][j], end=' ')


# In[ ]:

# Matrix 

