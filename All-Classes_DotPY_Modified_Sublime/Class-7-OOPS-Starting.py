
# coding: utf-8

# In[1]:

import sys
import re

if len(sys.argv) == 2:
    print(sys.argv[0], sys.argv[1])
    with open(sys.argv[1], 'r') as fp:
        linelist = fp.readlines()
        print(linelist)
        for line in linelist:
            i = linelist.index(line)
            if re.search('\s?\d+\.\s+\w+', line):
                linelist[i] = re.sub('\s?\d+\.\s', '', line)
            else:
                linelist[i] = re.sub('\s?\d+\.\s', '\n', line)
                
    print(linelist)
    with open('newdragon.py', 'w') as fp1:
        fp1.writelines(linelist)
    
else :
    print("Usage:-> strip_lnum filename.py")


# In[2]:

# Object Oriented Programming - OOPs puts objects at the center of the process. 


# In[3]:

# An object is sometimes referred to as an 'instance' of a class. 


# In[4]:

class pet: 
    number_of_legs = 0 # attribute of the class
    def eat(self): # method of the class
        print ('chop..chop...')


# In[5]:

doug = pet()


# In[6]:

doug.number_of_legs = 4


# In[7]:

print(doug.number_of_legs)


# In[20]:

tommy = pet()


# In[21]:

print(tommy.number_of_legs)


# In[22]:

print(doug.eat())


# In[30]:

# 2

class pet():
    number_of_legs = 4 # Initial value. 
    
    def sleep(self):
        print ("zzz")
        
    def count_legs(self):
        print ("I have %s legs" % self.number_of_legs)


# In[31]:

#1. 

doug = pet()
doug.number_of_legs = 10
print(doug.count_legs())


# In[32]:

#2. 

nemo = pet()
#nemo.number_of_legs = 2
print(nemo.count_legs())


# In[ ]:

# What this means is that wherever you write 'self' in your method, when you run the method 
# that self is replaced by the name of the object, so when you call 'doug.count_legs()' the 
# 'self' is replaced by 'doug'. 


# In[37]:

# 2

class pet():
    number_of_legs = 4 # Initial value. 
    
    def sleep(suman):
        print ("zzz")
        
    def count_legs(suman):
        print ("I have %s legs" % pet.number_of_legs)


# In[38]:

doug = pet()
doug.number_of_legs = 10
print(doug.count_legs())


# In[39]:

# Java constructor.

class pet():
    def __init__(self,name,species): # initializer
        self.name = name
        self.species = species
        
    def getName(self):
        return self.name
    
    def getSpecies(self):
        return self.species
    
    def __str__(self):
        return "%s is a %s" % (self.name,self.species)
    


# In[40]:

polly = pet("Polly","Parrot")


# In[42]:

print(polly.getName())


# In[44]:

print(polly.name)


# In[45]:

print(polly.species)


# In[46]:

print(polly)


# In[47]:

print(polly)


# In[54]:

# 
class Amitabh():
    superstar = 'yes'
    money = 'one billion'
    
class Abhishek(Amitabh):
    superstar = 'no'


# In[55]:

aradhya = Abhishek()


# In[56]:

print(aradhya.money)


# In[52]:

d1 = Amitabh()


# In[53]:

print(d1.superstar)


# In[ ]:



