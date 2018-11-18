
# coding: utf-8

# In[3]:

# desing 

class Pet():
    print ('Dog...')
    name = 'Tommy'


# In[4]:

object = Pet()


# In[5]:

object.name


# In[6]:

# Inheritance and Polymorphism


# In[9]:

class Teacher:
    def setid(self,id): # setter
        self.id = id
        
    def getid(self): # getter
        return self.id
    
    def setname(self,name): # setter
        self.name = name
        
    def getname(self): # getter
        return self.name
    
    def setaddress(self,address): # setter
        self.address = address
        
    def getaddress(self): # getter
        return self.address
    
    def setsalary(self,salary): # setter
        self.salary = salary
        
    def getsalary(self): # getter
        return self.salary
        


# In[10]:

t = Teacher() # create an object t


# In[12]:

t.setid(10)


# In[13]:

t.setname('Anuj')


# In[14]:

t.setaddress('111, Marine Drive, Florida - 18507')


# In[15]:

t.setsalary(15000)


# In[16]:

print ('id= ', t.getid())
print ('name= ', t.getname())
print ('address= ', t.getaddress())
print ('salary= ', t.getsalary())


# In[17]:

t2 = Teacher() # creating an object t2


# In[20]:

print ('id= ', t2.getid())
print ('name= ', t2.getname())
print ('address= ', t2.getaddress())
print ('salary= ', t2.getsalary())


# In[19]:

t2.setid(15)
t2.setname('Yuvi')
t2.setaddress('111, Marine Drive, Florida - 18507')
t2.setsalary(16000)


# In[21]:

class Student:
    def setid(self,id): # setter
        self.id = id
        
    def getid(self): # getter
        return self.id
    
    def setname(self,name): # setter
        self.name = name
        
    def getname(self): # getter
        return self.name
    
    def setaddress(self,address): # setter
        self.address = address
        
    def getaddress(self): # getter
        return self.address
    
    def setmarks(self,marks): # setter
        self.marks = marks
        
    def getmarks(self): # getter
        return self.marks


# In[22]:

s = Student()


# In[23]:

s.setid(15)
s.setname('Ashir')
s.setaddress('111, Marine Drive, Florida - 18507')
s.setmarks(900)


# In[24]:

print ('id= ', s.getid())
print ('name= ', s.getname())
print ('address= ', s.getaddress())
print ('marks= ', s.getmarks())


# In[25]:

pwd


# In[52]:

from teacher import Teacher

class Student2(Teacher):
    def setmarks(self,marks):
        self.marks = marks
        
    def getmarks(self):
        return self.marks
    
    def setsalary(self,salary,bonus):
        self.salary = salary
        Teacher.salary = salary
        self.bonus = bonus
        
    def getsalary(self):
        return self.salary    


# In[54]:

s2 = Student2()


# In[39]:

s2.setmarks(900)


# In[40]:

s2.getmarks()


# In[56]:

s2.setsalary(5000,100)


# In[41]:

class Teacher2:
    # constructor
    def __init__(self,id,name,address,salary):
        self.id = id
        self.name = name
        self.address = address
        self.salary = salary
    
    def setid(self,id): # setter
        self.id = id
        
    def getid(self): # getter
        return self.id
    
    def setname(self,name): # setter
        self.name = name
        
    def getname(self): # getter
        return self.name
    
    def setaddress(self,address): # setter
        self.address = address
        
    def getaddress(self): # getter
        return self.address
    
    def setsalary(self,salary): # setter
        self.salary = salary
        
    def getsalary(self): # getter
        return self.salary


# In[43]:

t2 = Teacher2(50,'Suman','xyz street',25000)


# In[44]:

print ('id= ', t2.getid())
print ('name= ', t2.getname())
print ('address= ', t2.getaddress())
print ('salary= ', t2.getsalary())


# In[20]:

class Bar():
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Foo(Bar):
    def __init__(self,id,name):
        super(Foo,self).__init__(id,name)
        self.baz = 5
        


# In[21]:

a = Foo(100,'suman')


# In[22]:

a.id


# In[70]:

# Overriding Super Class Constructors and Methods or attribute


# In[61]:

class Father:
    def __init__(self):
        self.property = 800000
        
    def display_property(self):
        print ("Father's property= ", self.property)
        
class Son(Father):
    pass


# In[62]:

s = Son()


# In[63]:

s.display_property()


# In[64]:

class Father:
    def __init__(self):
        self.property = 800000
        
    def display_property(self):
        print ("Father's property= ", self.property)
        
class Son(Father):
    def __init__(self):
        self.property = 200000
        
    def display_property(self):
        print ("Child's property= ", self.property)


# In[65]:

s2 = Son()


# In[66]:

s2.display_property()


# In[67]:

class Father2:
    def __init__(self):
        self.property = 800000
        
    def display_property(self):
        print ("Father's property= ", self.property)
        
class Son2(Father2):
    def __init__(self):
        self.property = 200000


# In[68]:

s3 = Son2()


# In[69]:

s3.display_property()


# In[71]:

# The super method 
# Multiple inheritance 

# Polymorphism


# In[ ]:



