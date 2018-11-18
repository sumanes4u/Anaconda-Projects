
# coding: utf-8

# In[1]:

class Celsius:
    def __init__(self,temperature=0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# In[2]:

man = Celsius()


# In[4]:

# Setting the temperature
man.temperature = 37


# In[5]:

# Get temperature
print(man.temperature)


# In[6]:

man.to_fahrenheit()


# In[7]:

print(man.__dict__)


# In[8]:

print(man.__dict__['temperature'])


# In[39]:

# Using Getters and Setters

class Celsius:
    def __init__(self,temperature=0):
        # The following codes though introduced as part of getter/setter, but it breaks the 
        # backward compatibility
        self.set_temperature(temperature)
        
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    # new update 
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self,value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
        
## get
#obj.temperature > obj.get_temperature()
# setting
#obj.temperature = val > obj.set_temperature()


# In[10]:

#c = Celsius(-277)  #---> ValueError: Temperature below -273 is not possible


# In[11]:

c = Celsius(37)


# In[12]:

c.get_temperature()


# In[13]:

c.set_temperature(10)


# In[14]:

c.get_temperature()


# In[15]:

#c.set_temperature(-300)  #--> ValueError: Temperature below -273 is not possible


# In[24]:

class test:
    public_key = 10
    _private = 20
    def private_method(self):
        print ('hi')
    


# In[25]:

a = test()


# In[26]:

test.public_key=20


# In[27]:

print(test.public_key)


# In[29]:

test._private=30


# In[30]:

print(test._private)


# In[35]:

class Celsius:
    def __init__(self,temperature = 0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    def get_temperature(self):
        print ("Getting value")
        return self._temperature
    
    def set_temperature(self,value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print ("Setting value")
        self._temperature = value
        
    # new The power of property
    temperature = property(get_temperature,set_temperature)


# In[36]:

c = Celsius()


# In[37]:

print(c.temperature)


# In[38]:

# The reason is that when an object is created, __init__() method gets called. This method has the
# the line 

# self.temperature = temperature. 

# The above assignment automatically calls set_temperature()


# In[40]:

# built-in property(). 

# property(fget=None,fset=None,fdel=None,doc=None)

# c.set_temperature


# In[51]:

class Celsius:
    def __init__(self,temperature = 0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    @property
    def temperature(self):
        print ("Getting value")
        return self._temperature
    
    @temperature.getter
    def test1():
        pass
    
    @temperature.setter
    def temperature(self,value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print ("Setting value")
        self._temperature = value


# In[42]:

c = Celsius()


# In[43]:

c.temperature = 30


# In[44]:

property()


# In[46]:

# a property object has three methods, getter(), setter() and delete(), to specify fget, fset, 
# fdel.

#temperature = property(get_temperature,set_temperature)

#and break down as 

#temperature = property()
#temperature = temperature.getter(get_temperture)
#temperature = temperature.setter(set_temperature)



# In[47]:

# iterator, closure, @decorator, @property, built-in method property() 


# In[67]:

# decorator
def star(func):
    def inner(*args,**kwargs):
        print ("*" * 30)
        func(*args,**kwargs)
        print("*" * 30)
    return inner
    
def percent(func):
    def inner(*args,**kwargs):
        print ("%" * 30)
        func(*args,**kwargs)
        print ("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("hello")

# the other way of writing the avove things
#def printer(msg):
#    print(msg)
#printer = star(percent(printer))
        


# In[55]:

def varags(*args,**kwargs):
    print(args)
    print(kwargs)


# In[56]:

varags(1,2,3,one=1,two=2,three=3)


# In[57]:

def tuple1(*args):
    print(args)


# In[58]:

tuple1(1,2,3)


# In[60]:

def dict1(**kwargs):
    print(kwargs)


# In[61]:

dict1(one=1,two=2,three=3)


# In[ ]:



