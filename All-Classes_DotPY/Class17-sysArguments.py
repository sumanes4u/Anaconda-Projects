
# coding: utf-8

# In[1]:

dir()


# In[2]:

import sys


# In[3]:

dir()


# In[4]:

from sys import argv


# In[5]:

dir()


# In[6]:

from sys import *


# In[7]:

dir()


# In[1]:

import sys
print ("script name is ", sys.argv[0])
if len(sys.argv) > 1:
    print ("there are", len(sys.argv)-1, "arguments:")
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("There are no arguments!")
    
print ("path has ", len(sys.path), "members")

print (sys.path)


# In[12]:

sys.path


# In[15]:

sys.path.insert(0,"/Users/aws")


# In[16]:

sys.path


# In[17]:

sys.path.append("/Users/aws")


# In[18]:

sys.path


# In[19]:

# packing and unpacking


# In[20]:

# packing a tuple

t1 = (1,2,3,4) # packing 


# In[21]:

t1


# In[22]:

a,b,c,d = t1 # unpacking


# In[23]:

a


# In[24]:

b


# In[25]:

c


# In[26]:

d


# In[30]:

list = [5,6,7,8]


# In[31]:

x,y,z,p = list


# In[32]:

x


# In[33]:

y


# In[34]:

x = 14


# In[35]:

list


# In[36]:

list2 = [7,8,9,10]


# In[37]:

x,y,z = list2


# In[ ]:



