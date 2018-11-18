
# coding: utf-8

# In[16]:

class Pet():
    
    hike = 1.5
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
class Dog(Pet):
    
    hike = 2.5 
    def __init__(self,a,b,c):
        self.a = a
        
    def int():
        print (hike)


# In[17]:

doug = Pet('t1','t2')
doug2 = Dog('t1','t2','t3')


# In[18]:

doug2.hike


# In[19]:

# multiple inheritance ( which java does not support but python supports)


# In[7]:

class Base1:
    hike = 1.5
    pass

class Base2:
    hike = 1.7

class MultiDerived(Base1,Base2):
    hike = 2.0
    pass

obj1 = MultiDerived()


print (obj1.hike)

# MRO = Method Resoltion Order in Python


# In[21]:

MultiDerived.__mro__


# In[26]:

class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z):pass

print(M.mro())



# In[1]:

class Customer(object):
    
    def __init__(self,name):
        self.name = name
    
    def set_balance(self,balance=0.0):
        self.balance = balance
        
    def withdraw(self,amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance')
        self.balance -= amount
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
        



# In[2]:

raj = Customer('Raj')


# In[3]:

raj.set_balance(500)


# In[54]:

raj.withdraw(100)


# In[55]:

raj.deposit(200)


# In[56]:

raj.withdraw(1000)


# In[ ]:



