
# coding: utf-8

# In[1]:

#- operator overloading
#- Method overloading 
#- Method overriding
#- Duck typing philosophy

# in Java

#int(age)
age = 15



# In[2]:

x = 5 

print (type(x))


# In[3]:

x = 'Hello'
print (type(x))


# In[ ]:

def call_talk(obj): # this function is recieving an 'obj' from outside, and using this object, and invoking obj.talk().
    obj.talk()


# In[8]:

#1
class Duck:
    def talk(self):
        print ('Quack, quack!')
#2        
class Human:
    def talk(self):
        print ('Hello,Hi!')
#3        
def call_talk(obj):
    obj.talk()


# In[5]:

x = Duck()


# In[6]:

call_talk(x)


# In[7]:

x = Human()
call_talk(x)


# In[9]:

x = Duck()
call_talk(x)


# In[10]:

class Dog:
    def bark(self):
        print ('Bow,wow!')
        
class Duck:
    def talk(self):
        print ('Quack, quack')
        
class Human:
    def talk(self):
        print ('Hello, hi')
        
def call_talk(obj):
    obj.talk()


# In[11]:

# call call_talk() method and pass an object depending on type of object, talk() method is executed.


# In[12]:

x = Duck()


# In[13]:

call_talk(x)


# In[14]:

x = Human()


# In[15]:

call_talk(x)


# In[16]:

x = Dog()


# In[17]:

#call_talk(x)


# In[19]:

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()


# In[22]:

x = Dog() # create a object


# In[21]:

call_talk(x)


# In[27]:

class Pet():
    # attribute
    legs = 4
    # method
    def sound():
        print ('sound...')


# In[34]:

# hasattr(object,attribute), it will look for attributes and methods


# In[29]:

z = Pet()


# In[37]:

hasattr(z,'sound')


# In[38]:

class Dog:
    def bark(self):
        print ('Bow,wow!')
        
class Duck:
    def talk(self):
        print ('Quack, quack')
        
class Human:
    def talk(self):
        print ('Hello, hi')
        
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
    else:
        print ('Wrong object passed...')


# In[39]:

x = Duck()


# In[40]:

call_talk(x)


# In[41]:

x = Human()


# In[42]:

call_talk(x)


# In[43]:

x = Dog()


# In[44]:

call_talk(x)


# In[45]:

x = Pet()


# In[46]:

call_talk(x)


# In[47]:

# Operator Overloading 


# In[48]:

2 + 2


# In[49]:

3 * 4


# In[50]:

print (10+15)


# In[51]:

# use the same + to concatenate them


# In[52]:

s1 = "Red"
s2 = "Fort"


# In[53]:

print (s1 + s2)


# In[54]:

a = [10,20,30]
b = [5,15,-10]


# In[55]:

print ( a + b)


# In[ ]:

#+ 
 #- adding two integers
 #- adding two strings
 #- adding two lists
    
#Any operator performs additional actions other than what it is meants for, it is called operator overloading. 
#This operator overloading is an example for polymorphism. 


# In[ ]:

#two objects , obj1 + obj2 

#b1 = BookX(100)
#b2 = BookY(150)
#b1 + b2 = 250 


# In[57]:

class BookX:
    def __init__(self,pages):
        self.pages = pages
        
class BookY:
    def __init__(self,pages):
        self.pages = pages


# In[58]:

b1 = BookX(100)


# In[59]:

b2 = BookY(150)


# In[60]:

#print ('Total pages= ', b1 + b2 )  #This cannot add the pages


# In[ ]:

#+ = __add__()
#a + b = a.__add__(b)


# In[61]:

a = 2
b = 3


# In[62]:

a + b # simple


# In[63]:

a.__add__(b) # complicated.


# In[ ]:

# Override 
def __add__(self,other):
    return self.a+other.b


# In[ ]:

def __add__(self,other):
    return self.pages + other.pages


# In[64]:

# overloading + operator

class BookX:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages + other.pages
    
class BookY:
    def __init__(self,pages):
        self.pages = pages


# In[65]:

b1 = BookX(100)
b2 = BookY(150)
print ('Total pages= ', b1+b2)


# In[66]:

# pythom operator and corrsponding Magic Methods


# In[ ]:

#+  object.__add__(self,other)

#-  object.__sub__(self,other)

#> object.__gt__(self,other)


# In[67]:

class ScienceBook:
    def __init__(self,pages):
        self.pages = pages
        
    def __gt__(self,other):
        return self.pages > other.pages
    
class ArtsBook:
    def __init__(self,pages):
        self.pages = pages


# In[68]:

b1 = ScienceBook(1000)


# In[69]:

b2 = ArtsBook(1500)


# In[70]:

if (b1 > b2):
    print ('ScienceBook has more pages')
else:
    print ('Arts has more pages')


# In[ ]:

def __mul__(self,other):
    return self.salary * other.days


# In[71]:

# Method Overloading 


# In[73]:

#sum('10','15')


# In[74]:

help(sum)


# In[75]:

#doc(sum)


# In[76]:

list = [2,3,4]


# In[3]:

sum(list)


# In[2]:

sum(list,5)


# In[80]:

# method overloading

class Myclass:
    def sum(self,a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print ('Sum of three= ', a+b+c)
        elif a != None and b != None:
            print ('Sum of two= ', a+b)
        else:
            print ('Please enter two or three arguments instead')


# In[81]:

m = Myclass()


# In[82]:

m.sum(10,15,20)


# In[83]:

m.sum(10,15)


# In[84]:

m.sum(10)


# In[85]:

# method overloading


# In[ ]:

#def func()
 #   print (a)
 #   print (a+b)
 #   print (a+b+c)
 #   print (a+b+c+d)


# In[86]:

# Method overriding


# In[92]:

import math
class Square:
    def area(self,x):
        print ('Square area = %.4f' % x*x)

class Circle(Square):
    def area(self,x): # Overriding the area method with something enhanced or extra
        print ('Square area = %.4f' % math.pi*x*x)    


# In[88]:

c = Circle()


# In[90]:

s = Square()


# In[91]:

s.area(15)


# In[89]:

c.area(15)


# In[93]:

# Abstract classes and interfaces


# In[94]:

class Myclass:
    def calculate(self,x):
        print ('Square value =', x*x)


# In[95]:

obj1 = Myclass()


# In[96]:

obj1.calculate(2)


# In[97]:

obj2 = Myclass()


# In[98]:

obj2.calculate(3)


# In[99]:

# abstract method 


# In[100]:

from abc import ABC, abstractmethod


# In[113]:

from abc import ABC, abstractmethod
class Myclass(ABC): # Myclass is an abstract class because it is derived from ABC meta class. 
    
    @abstractmethod
    def calculate(self,x): # abstract method 
        pass # empty body , no code
    
import math

class Sub1(Myclass):
    def calculate(self,x):
        print ('Square value=', x*x)
        

class Sub2(Myclass):
    def calculate(self,x):
        print ('Square root=', math.sqrt(x))
        

class Sub3(Myclass):
    def calculate(self,x):
        print ('Cube value=', x**3)


# In[107]:

obj1 = Sub1()


# In[108]:

obj1.calculate(16)


# In[111]:

obj2 = Sub2()


# In[112]:

obj2.calculate(16)


# In[118]:

from abc import ABC, abstractmethod
class Father(ABC): # Myclass is an abstract class because it is derived from ABC meta class. 
    @abstractmethod
    
    def give_money(self,x): # abstract method 
        pass # empty body , no code
    
import math

class Son1(Father):   # Implemention
    def give_money(self,x):
        print ('Buys a Car=',x )
        

class Son2(Father):
    def give_money(self,x):
        print ('Buys a Home=', x)
        

class Son3(Father):
    def give_money(self,x):
        print ('Invest in stock', x)
        
class Son4(Father):
    def give_money(self,x):
        print ('Invest in stock', x)
    


# In[119]:

son4 = Son4()


# In[120]:

# interface 


# In[ ]:



