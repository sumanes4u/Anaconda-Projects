
# coding: utf-8

# # Class 
#  - Constructor ( init method )
#  - Namespaces
#  - types of methods 
#     - Instance methods
#     - class methods
#     - static methods
#     - Inner Classes
#     - Inheritance
#     - Polymorphism
#     - Method overloading

# In[3]:

class Sample:
    
    # This is a constructor
    def __init__(self):
        self.x = 10
        
    # this is an instance method 
    def modify(self):
        self.x += 1 # ( x = x + 1)


# In[4]:

# create two instances
s1 = Sample()
s2 = Sample()


# In[5]:

print ('x in s1= ', s1.x)
print ('x in s2= ', s2.x)


# In[6]:

# modify x in s1
s1.modify()


# In[7]:

print ('x in s1= ', s1.x)
print ('x in s2= ', s2.x)


# In[8]:

# class variable vs static variables


# In[17]:

class Sample2:
    
    # This is a constructor
    def __init__(self,var1,var2,var3,var4):
        self.x = 10
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.var4 = var4
        
    # this is an instance method 
    def modify(self):
        self.x += 1 # ( x = x + 1)
        
    def method1(self):
        print (self.var1)
        
    def method2(self):
        print (self.var2)
        
    def method3(self):
        print (self.var3)
        
    def method4(self):
        print (self.var4)


# In[20]:

s3 = Sample2('a','b','c','d') # instance/object creation 


# In[19]:

s3.method4()


# In[21]:

# instance method or instance variable 


# In[22]:

# class variables or static variables 


# In[27]:

class Sample3:
    # this is a class var
    x = 10
    
    # this is a class method
    @classmethod # decorator
    def modify(cls):
        cls.x += 1
        
# create 2 instaances 
    
s1 = Sample3()
s2 = Sample3()
    
print ('x in s1 = ', s1.x)
print ('x in s2 = ', s2.x)
    
# modify x in s1 
    
s1.modify()
print ('x in s1 = ', s1.x)
print ('x in s2 = ', s2.x)
    
    


# In[28]:

# Namespace

class Student():
    n = 10


# In[29]:

print (Student.n)


# In[30]:

Student.n += 1


# In[31]:

print (Student.n)


# In[32]:

s1 = Student()


# In[33]:

s1.n


# In[34]:

s2 = Student()


# In[35]:

s2.n


# In[36]:

s1.n = 20


# In[37]:

s2.n


# In[38]:

s1.n


# In[42]:

class Student:
    # This is a constructor
    
    def __init__(self,n='',m=0):
        self.name = n
        self.marks = m
        
    # instance method
    
    def display(self):
        print ('HI',self.name)
        print ('Your marks', self.marks)
        
    # to calculate grades
    
    def calculate(self):
        if (self.marks >= 600):
            print ('First Grade')
        elif (self.marks >= 500):
            print ('Second Grade')
        elif (self.marks >= 350):
            print ('Third Grade')
        else:
            print ('You got failed')
            
n = int(input('How many students? '))

i = 0

while(i < n):
    name = input('Enter name: ')
    marks = int(input("Enter marks: "))
    
    # create Student class instance and store data
    s = Student(name,marks)
    s.display()
    s.calculate()
    i += 1
    print ('...................')


# In[ ]:

# Instance method : 
 #Two types : 1) accessor method 2) mutator method 
        
A#ccessor method - simple access or read data of the variable. getABC() # getter methods

            


# In[56]:

# getter # Accessor method
def getName(self):
    return self.name


# In[ ]:

# setter setABC() # Mutator method
def setname(self,name):
    self.name = name # setting some value


# In[60]:

class Student:
    
    # mutator method 
    def setName(self,name):
        self.name = name
          
    # Accessro method
    
    def getName(self):
        return self.name
    
    # mutator method
    
    def setMarks(self,marks):
        self.marks = marks
        
    # accessor method
    
    def getMarks(self):
        return self.marks
    
n = int(input('How many students? '))

i = 0

while(i < n):
    s = Student()
    name = input('Enter name: ')
    s.setName(name)
    
    marks = int(input("Enter marks: "))
    s.setMarks(marks)
    
    # retrieve the data
    print ('Hi ', s.getName())
    print ('Your marks', s.getMarks())

    i += 1
    print ('...................')


# In[61]:

# class methods
# static methods


# In[64]:

class Bird():
    wings = 2
    
    @classmethod
    def fly(cls,name):
        print('{} flies with {} wings'.format(name,cls.wings))
        
Bird.fly('Sparrow')
Bird.fly('Pigeon')


# In[65]:

# static method


# In[69]:

class Myclass:
    n = 0 # class variable or static var
    
    def __init__(self):
        Myclass.n = Myclass.n+1
        
    @staticmethod
    def noObject():
        print ('No. of instance created: ', Myclass.n)
        
obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj3 = Myclass()



Myclass.noObject()


# In[ ]:



