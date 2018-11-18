
# coding: utf-8

# In[1]:

# Matrices in numpy


# In[ ]:

#matrix-name = matrix(2D array or string)


# In[2]:

arr = [[1,2,3],[4,5,6]]


# In[4]:

from numpy import *
a = matrix(arr)


# In[5]:

a


# In[7]:

from numpy import *
a = matrix([[1,2,3],[4,5,6]])


# In[8]:

a


# In[9]:

str = '1 2; 3 4; 5 6'


# In[10]:

b = matrix(str)


# In[11]:

b


# In[12]:

b = matrix("1 2; 3 4; 5 6")


# In[13]:

b


# In[14]:

# Diagonal Element


# In[16]:

# a = diagonal(matrix)


# In[17]:

a = matrix('1 2 3; 4 5 6;7 8 9') # 3 * 3 Matrix


# In[18]:

a


# In[19]:

d = diagonal(a)


# In[20]:

d


# In[21]:

# Finding Maximum and Minimum Elements


# In[22]:

big = a.max()


# In[23]:

big


# In[24]:

small = a.min()


# In[25]:

small


# In[26]:

a.sum()


# In[27]:

a.mean()


# In[28]:

# Product of Elements


# In[29]:

m = matrix(arange(12).reshape(3,4))


# In[30]:

m


# In[31]:

m.prod(0)


# In[33]:

m.prod(1)


# In[34]:

# sorting the matrix


# In[35]:

# sort(matrixname,axis)

# axis = 1, it sorts the elements in each row into ascendending order.  # default value. 
# axis = 0, it sorts the elements in each column into ascendending order. 


# In[36]:

m = matrix([[5,4,1],[2,7,0]])


# In[37]:

print (m)


# In[38]:

a = sort(m)
print (a)


# In[39]:

b = sort(m, axis=0)
print (b)


# In[41]:

# Transpose of a Matrix : Rewriting matrix rows into coumns and vice versa. 


# In[42]:

m = matrix('1 2 3; 4 5 6; 7 8 9')
print (m)


# In[43]:

t = m.transpose()


# In[44]:

print (t)


# In[45]:

t1 = m.getT()
print (t1)


# In[46]:

# ex

from numpy import * 

r , c = [int(a) for a in input("Enter rows, cols: ").split()]

str = input('Enter matrix elements: \n')

# convert the string into matrix with size r * c

x = reshape(matrix(str), (r,c))
print ('The original matrix: ')
print (x)

print ('The transpose matrix: ')
y = x.transpose()
print (y)


# In[47]:

# Matrix addition and multiplication 


# In[48]:

a = matrix('1 2 3; 4 5 6')
b = matrix('2 2 2; 1 -1 2')
print (a)


# In[49]:

print(b)


# In[50]:

c = a + b
print (c)


# In[51]:

d = a/b
print (d)


# In[52]:

# ex 



# In[56]:

import sys
from numpy import * 

r1 , c1 = [int(a) for a in input("Enter rows, cols: ").split()]

r2 , c2 = [int(a) for a in input("Enter rows, cols: ").split()]

if c1 != r2: 
    print ('Multiple is not possible')
    sys.exit()
    
str1 = input('Enter the first matrix elements: \n')

x = reshape(matrix(str1),(r1,c1))

str2 = input('Enter the second matrix elements: \n')

y = reshape(matrix(str2),(r2,c2))

print ('The product matrix: ')

z = x * y
print (z)


# In[57]:

# Random Numbers


# In[61]:

random.rand()


# In[62]:

a = random.rand(5)


# In[63]:

a


# In[64]:

b = random.rand(2,3)
print (b)


# In[ ]:

# Numpy
# - Arrays
# - arange
# - zeros and ones
# - linspace
# - logspace
# - eye
#- random ( randn and randint)
#- reshape, shape
#- max, min, argmax, argmin
# - transpose
# - dtype
# - indexing and , selection, slicing
# - Broadcasting
# - all arithmeticatic operation. 


# In[67]:

import numpy as np
arr = np.arange(0,11)
print (arr)


# In[68]:

arr[0:5] = 100
print (arr)


# In[ ]:



