
# coding: utf-8

# In[1]:

# The super() method


# In[ ]:

# __init__()

#super()__init__()
#super()__init__(arguments)
#super().method() # call super class method


# In[ ]:

# we're defining into a sub class ie child class
def __init__(self,property1=0,property=0):
    super().__init__(property) # send property value to super class 
    
    # constructor
    self.property1 = property1 # store proerty1 value into sub class


# In[ ]:

#s = Son(2000000,8000000)


# In[2]:

def func1(arg1=0,arg2=1):
    print (arg1)
    print (arg2)


# In[4]:

func1(2,4)


# In[13]:

class Father():  
    def __init__(self,name,age):
        self.name = name # means that we're storing the value in this class
        print (name)
        
    def test():
        print (self.name) # utilization


# In[22]:

class Father():
    def __init__(self,property=0):
        self.property = property
        
    def display_property(self):
        print ("Father's property= ", self.property)
        
class Son(Father):
    def __init__(self,property1=0, property=0):
        super().__init__(property)
        self.property1 = property1
        
    def display_property(self):
        print ('Total property of child= ', self.property1 + self.property)
    


# In[23]:

s = Son(200000,800000)


# In[24]:

s.display_property()


# In[30]:

# 
class Square:
    def __init__(self,x):
        self.x = x
        
    def area(self):
        print ('Area of square= ', self.x * self.x)
        
class Rectangle(Square):
        def __init__(self,x,y):
            super().__init__(x) # we're calling super class init method and passing the argument as x. 
            self.y = y
            
        def area(self):
            super().area() # important 
            print ('Area of rectange= ', self.x * self.y)
            
a, b = [float(x) for x in input("Enter two arguments: ").split()] # list comprehension
r = Rectangle(a,b)
r.area()


# In[31]:

x = 5


# In[32]:

x


# In[34]:

type(x)


# In[35]:

f = float(x)


# In[36]:

f


# In[ ]:

# Types inheritance 

#- Father       --       Son
#- Mother       --


# In[42]:

class Father():
    def height(self):
        print ("Height is 6.0 foot")
        
class Mother():
    def color(self):
        print ('Color is White')
    
class Child(Father,Mother): # Multiple Inheritance 
    pass


# In[39]:

c = Child()


# In[40]:

c.color()


# In[41]:

c.height()


# In[43]:

# problem with multiple inheritance


# In[46]:

# Type 1 
class A(object):
    def __init__(self):
        self.a = 'a'
        print (self.a)
        
class B(object):
    def __init__(self):
        self.b = 'b'
        print (self.b)
        
class C(A,B):
    def __init__(self):
        self.c = 'c'
        print (self.c) # this c get printed. 
        super().__init__() #


# In[45]:

o = C()


# In[47]:

# Type 2
class A(object):
    pass
        
class B(object):
    def __init__(self):
        self.b = 'b'
        print (self.b)
        
class C(A,B):
    def __init__(self):
        self.c = 'c'
        print (self.c) # this c get printed. 
        super().__init__() #


# In[48]:

o2 = C()


# In[49]:

# Type 3
class A(object):
    def __init__(self):
        self.a = 'a'
        print (self.a)
        
class B(object):
    def __init__(self):
        self.b = 'b'
        print (self.b)
        
class C(B,A):
    def __init__(self):
        self.c = 'c'
        print (self.c) # this c get printed. 
        super().__init__() #


# In[50]:

o3 = C()


# In[51]:

# Type 4 

class A(object):
    def __init__(self):
        self.a = 'a'
        print (self.a)
        super().__init__()
        
class B(object):
    def __init__(self):
        self.b = 'b'
        print (self.b)
        super().__init__()
        
class C(A,B):
    def __init__(self):
        self.c = 'c'
        print (self.c) # this c get printed. 
        super().__init__() #


# In[52]:

o4 = C()


# In[53]:

# MRO - Method resolution order 


# In[ ]:




# In[54]:

class A(object):
    def method(self):
        print ('A class method')
        super().method()
class B(object):
    def method(self):
        print ('B class method')
        super().method()
class C(object):
    def method(self):
        print ('C class method')
class X(A,B):
    def method(self):
        print ('X class method')
        super().method()
class Y(B,C):
    def method(self):
        print ('Y class method')
        super().method()
class P(X,Y,C):
    def method(self):
        print ('P class method')
        super().method()


# In[55]:

p = P()


# In[56]:

p.method()


# In[57]:

P.mro()


# In[ ]:

# Polymorphism

