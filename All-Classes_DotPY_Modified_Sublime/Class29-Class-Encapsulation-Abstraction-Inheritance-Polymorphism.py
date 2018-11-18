
# coding: utf-8

# In[6]:

# Oriented concept
def main_function():
    
    def func1():
        print ('func1...')
        
    def func2():
        print ('func1...')
        
    def func3():
        print ('func1...')
        
    func1() # calling the function. 
    func2()
    func3()


# In[7]:

main_function()


# # OOPS - Object Oriendted Programming System
# 
# class - design - recipe (one)
#    - object - instance - mutter paneer
#     
# attribute
# method
# 
# - Person
#    attribute ( name, age, sex...)
#    actions ( talking,walking, eating..)
# 
# object 
#    - variables
#    - methods
# 

# In[8]:

class Person:
    # attributes or variables
    name = 'Raj'
    age = 20
    
    # actions 
    def talk(cls):
        print (cls.name)
        print (cls.age)


# In[9]:

# create an object

p1 = Person()


# In[10]:

p1.age


# In[11]:

p1.name


# In[12]:

p1.talk()


# In[13]:

p2 = Person()


# In[14]:

p2.age


# # oops
#  - classes and objects
#  - Encapsulation
#  - Abstraction
#  - Inheritance
#  - Polymorphism

# In[15]:

# Encapsulation


# In[16]:

class student:
    # declare and initialize the variables
    
    def __init__(self):
        self.id = 10 # attribute, and initial value
        self.name = 'Raju'  # attribute and initial value
        
    def display(self):
        print(self.id)
        print (self.name)


# In[17]:

suman = student()


# In[18]:

suman.id


# In[19]:

suman.name


# In[20]:

suman.display()


# In[21]:

suman.id = 20


# In[22]:

suman.display()


# In[23]:

krishna = student()


# In[24]:

krishna.display()


# In[25]:

# Abstraction ( hiding )

class Myclass:
    
    def __init__(self):
        self.__y = 3 # this is a private variable


# In[26]:

p3 = Myclass()


# In[27]:

#p3.y    #This will not be able to access the protected attribute


# In[29]:

p3._Myclass__y # This is how we access private variable y


# In[32]:

class Myclass:
    # constructor 
    def __init__(self):
        self.x = 1 # public variable
        self.__y = 2 # private variable
        
    def display(self):
        print (self.x)
        print (self._Myclass__y)


# In[33]:

m = Myclass()


# In[39]:

m.display() # accessing it via method


# In[35]:

m.x # accessing it via attribute


# In[40]:

m._Myclass__y # accessing it via attribute


# In[45]:

# 

class Bank : 
    def __init__(self):
        self.accno = 10
        self.name = 'Raj'
        self.balance = 5000
        self.__loan = 150000 # private, should not be visible to clerk
        
    def display_to_clerk(self):
        print (self.accno)
        print (self.name)
        print (self.balance)
        #print (self.loan)


# In[46]:

cust1 = Bank()


# In[47]:

cust1.display_to_clerk()


# In[48]:

# Inheritance 


# In[70]:

class A:
    a = 1 # class variable 
    b = 2 # class variable 
    
    def method1(A):
        print (A.a)
        print (A.b)
        
class B(A):
    c = 3
    def method2(A):
        print (A.c)


# In[54]:

x = A()


# In[55]:

x.a


# In[68]:

y = B()


# In[69]:

y.a


# In[66]:

y.b


# In[61]:

y.c


# In[71]:

class A:
    a = 1 # class variable 
    b = 2 # class variable 
    
    def method1(cls):
        print (cls.a)
        print (cls.b)
        
class B(A):
    c = 3
    def method2(cls):
        print (cls.c)


# In[72]:

obj1 = A()


# In[73]:

obj2 = B()


# In[77]:

obj1.a = 5


# In[78]:

obj2.a


# In[75]:

obj2.c


# In[79]:

# Polymorphism


# In[81]:

def add(a,b):
    print (a+b)


# In[85]:

def add(a,b):
    print (a+b)
    
add(5,10) # adding integers


# In[86]:

add("ABC",'Python') # addging strings


# In[87]:

# Any programming language which follows OOPS. C++, Java and Python


# In[ ]:



