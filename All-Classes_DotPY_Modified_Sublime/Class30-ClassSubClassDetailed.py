
# coding: utf-8

# In[7]:

# general format class

class Classname(object):
    """ This is my custom class"""
    
    #attributes 
    name = 'raj'
    age = 15
    
    # methods
    def __init__(self):
        pass
    
    def method1():
        pass
    
    def method2():
        pass
    


# In[14]:

class Student:
    def __init__(self):
        self.name = 'Raj'
        self.age = 20
        self.marks = 90
        
    def talk(self):
        print ("hi, My name is " + self.name)
        print ('My age is ', self.age)
        print ('My marks is ', self.marks)
        
    


# In[15]:

s1 = Student()
s2 = Student()
s3 = Student()


# In[18]:

s1.talk()


# In[17]:

s1.name = 'Suman'
s1.age = 25
s1.marks = 90


# In[28]:

class Bank:
    def __init__(self,name,age):
        self.balance = 100 # Business use case 
        self.name = name
        self.age = age
        
        
    def check_balance(self):
        print ('Your balance is', self.balance)
    
    def my_profile(self):
        print ('name is', self.name)
        print ('age is ', self.age)


# In[29]:

ac1 = Bank('Suman',25)


# In[30]:

ac1.age


# In[31]:

ac2 = Bank('Ashir',26)


# In[32]:

ac2.age


# In[59]:

class Bank:
    
    balance = 50 # class variable 
    
    def __init__(self,name,age,amount):
        self.balance = 100 # Business use case # instance variable
        self.name = name
        self.age = age
        self.amount = amount
        
    def check_balance(self):
        print ('Your balance is', self.balance)
        
    def deposit(self):
        self.balance += self.amount
        print ('My balance is ', self.balance)
        
    def withdrawal(self):
        if self.balance <= self.amount:
        # if self.balance <= 0:
            print ('You dont enough balance to take out cash')
        else:
            self.balance -= self.amount
            print ('My balance is ', self.balance)
    
    def my_profile(self):
        print ('name is', self.name)
        print ('age is ', self.age)
ac1 = Bank('Raj',22,50)
ac2 = Bank('Anuj',26,40)

ac2.age = 27

ac2.withdrawal()
ac2.withdrawal()
ac2.withdrawal()


# In[55]:

ac3 = Bank('Anuj',22,50)


# In[37]:

ac3.check_balance()


# In[38]:

ac3.deposit() # method you're performing a trasaction


# In[39]:

ac3.deposit()


# In[40]:

ac3.amount = 400


# In[41]:

ac3.deposit()


# In[43]:

ac3.amount = 100


# In[46]:

ac3.withdrawal()


# In[47]:

ac3.withdrawal()


# In[51]:

ac3.withdrawal()


# In[52]:

ac3.withdrawal()


# In[58]:

ac3.withdrawal()


# In[68]:

class student:
    age = 50
    # This is a constructor 
    def __init__(self,n='',m=0):
        self.name = n
        self.marks = m
        
        
    # this is an instance method
    
    def display(self):
        print ('Hi',self.name)
        print ('You marks',self.marks)
        print ('My age is ', student.age)


# In[69]:

s = student()


# In[70]:

s.display()


# In[63]:

s1 = student('Krishna Reddy',500)


# In[71]:

s1.display()


# In[1]:

class Sample:
    x = 10 # class variable
    def __init__(self):
        self.x = 10
        
    # instance method
    def modify(self):
        #self.x += 1
        Sample.x +=1
        


# In[2]:

s1 = Sample()


# In[3]:

s2 = Sample()


# In[4]:

print ('x in s1 = ',s1.x)
print ('x in s2 = ',s2.x)


# In[5]:

s1.modify()
print ('x in s1 = ',s1.x)
print ('x in s2 = ',s2.x)


# In[6]:

s1.modify()
print ('x in s1 = ',Sample.x)
print ('x in s2 = ',Sample.x)


# In[ ]:




# In[ ]:



