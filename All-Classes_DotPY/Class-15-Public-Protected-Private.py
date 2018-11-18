
# coding: utf-8

# In[1]:

class Hotel(object):
    
    def pay(self):
        print ("Paid")
        return self
        
    
    def order(self):
        print ("Order")
        return self
    
    def eat(self):
        print ("Ate")
        return self
    
    def feedback(self):
        print ("Feedback")
        return self
    

        


# In[2]:

TajHotel = Hotel()


# In[3]:

TajHotel.pay().order().eat().feedback() # Method chaining


# In[20]:

def test1():
    print ('2')


# In[21]:

a = test1()


# In[22]:

a


# In[26]:

class Hotel(object):
    
    def pay(self):
        print ("Paid")
        return self


# In[27]:

TajHotel = Hotel()


# In[31]:

a = TajHotel.pay()


# In[32]:

type(a)


# In[33]:

# Private, protected and public 

class Cup:
    def __init__(self):
        self.color = None
        self.content = None
        
    def fill(self,beverage):
        self.content = beverage
        
    def empty(self):
        self.content = None
        


# In[34]:

redCup = Cup()


# In[35]:

redCup.color = 'red'


# In[36]:

redCup.content = 'tea'


# In[38]:

redCup.content


# In[39]:

redCup.empty()


# In[40]:

redCup.content


# In[43]:

redCup.fill("Coffee")


# In[44]:

redCup.content


# In[45]:

# Protected. 

class Cup:
    def __init__(self):
        self.color = None
        self._content = None
        
    def fill(self,beverage):
        self._content = beverage
        
    def empty(self):
        self._content = None


# In[46]:

cup = Cup()


# In[47]:

cup._content = 'tea'


# In[48]:

cup._content


# In[50]:

# Private

class Cup:
    def __init__(self,color):
        self._color = None # protected
        self.__content = None # private
        
    def fill(self,beverage):
        self.__content = beverage
        
    def empty(self):
        self.__content = None


# In[52]:

greenCup = Cup('Green')


# In[53]:

greenCup.__content  # this is not visiable 


# In[57]:

# _<className><memberName> # with this way, it is visible via class, and not directly via object. 

greenCup._Cup__content = 'tea' # We dont do it. 


# In[58]:

greenCup._Cup__content 


# In[59]:

# Static Variable and Methods in Python

# Static means, the the member is on a class level rather than the instance level. Static 
# variable exist only in single instance per class and not instantiated. 

# Class or object. 

# Members: 

# 1. Attribute/Variable
# 2. Method



# In[69]:

class Example:
    variable = 5 # Access through class
    
    def test(self,variable):
        self.variable = variable


# In[70]:

Example.variable


# In[71]:

Instance = Example()


# In[72]:

Instance.variable


# In[73]:

Instance.variable = 10


# In[74]:

Instance.variable


# In[75]:

# @staticmethod


# In[76]:

class Example:
    name = 'Example'
    
    @staticmethod
    def static():
        print ("%s static() called" % Example.name)
        
class Offspring1(Example):
    name = "Offspring1"
    
class Offspring2(Example):
    name = "Offspring2"
    
    @staticmethod
    def static():
        print ("%s static() called" % Offspring2.name)
        
    


# In[77]:

Example.static()


# In[78]:

Offspring1.static()


# In[79]:

Offspring2.static()


# In[80]:

# @classmethod

class Example:
    name = 'Example'
    
    @classmethod
    def static(cls):
        print ("%s static() called" % cls.name)
        
class Offspring1(Example):
    name = "Offspring1"
    
class Offspring2(Example):
    name = "Offspring2"
    
    @classmethod
    def static(cls):
        print ("%s static() called" % cls.name)


# In[81]:

class Student:
    stream = 'cse' # Class Variable 
    
    def __init__(self,name,roll):
        self.name = name   # Instance Variable
        self.roll = roll   # Instance Variable
        
        


# In[ ]:

#Both @classmethod and @staticmethod are similar. The difference (slight) difference in usage . @classmethod must have 
# a reference to a class object as the first parameter, where @staticmethod can have no parameters at all. 

