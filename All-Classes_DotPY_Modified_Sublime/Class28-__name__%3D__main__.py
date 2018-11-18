
# coding: utf-8

# In[1]:

# The Special Variable : __name__


# In[2]:

def toeat():
    print ('eating....')


# In[4]:

toeat()
# Python internally creates __name__ variable. 


# In[5]:

# Stores information regarding whether the program is executed as an individual program or as a module. 


# In[6]:

import math


# In[7]:

# When the program is executed directly, the python interpreter stores the value '__main__' into this '__name__' 
# variabel. 

# When the program program is imported a module into another program, then Python interpreter stores the module name 
# this variable. '__name__' value .


# In[8]:

if __name__ == '__main__':
    print ('This code is run as a program')


# In[9]:

#pwd


# In[10]:

dir()


# In[11]:

from work import towork


# In[12]:

dir()


# In[20]:

def display():
	print ('Hello Python')
	
if __name__ == '__main__':
	display() # calls the display function
	print ('This code is run as a program')
else:
	print ('This code is run as a module')
    
print (__name__)


# In[24]:

import one


# In[22]:

one.display()


# In[23]:

print (one.__name__)


# In[25]:

#
import sys


# In[26]:

sys.path.insert(0,'/Users')


# In[ ]:



