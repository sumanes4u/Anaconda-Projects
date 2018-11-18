
# coding: utf-8

# In[ ]:

# practical example
'''
class Bank():
    
#or 
    
class Bank():
    
Father
  - Son
    - his son
      - his son2
        
class Father(object) # parent class 

class Son(Father)

class his_son(Son)

class his_son2(his_son)

'''

# In[10]:

class Bank(object):
    
    # initialize
    
    def __init__(self,name, balance = 0.0):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance # missing. 
        
    def withdraw(self,amount):
        if amount > self.balance:
            print ('Balance amount is less, so no withdrawal.')
        else:
            self.balance -= amount
        return self.balance
    


# In[13]:

# create an object of the class
import sys

name = input('Enter name: ')
b = Bank(name)

while(True): # infinite
    print ('d - Deposit, w - withdraw, e - Exit')
    choice = input('Your choice: ')
    
    if choice == 'e' or choice == 'E':
        # break
        sys.exit()
        
    # amount for deposit or withdraw
    
    amt = float(input('Enter amount: '))
    
    # main transaction 
    
    if choice == 'd' or choice == 'D':
        print ('Balance after deposit: ', b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print ('Balance after withdrawal: ', b.withdraw(amt))
        


# In[4]:

b = Bank('Raj')


# In[5]:

b.deposit(100) # what is the parent of this object/instance. 


# In[7]:

b.balance


# In[8]:

b.deposit(200)


# In[9]:

b.balance


# In[14]:

class Emp():
    pass


# In[15]:

e = Emp()


# In[16]:

type(e)


# In[22]:

isinstance(e,Emp)


# In[ ]:

def mymethod(e):
    
    e.salary += 1000
    e.display()


# In[ ]:

Myclass.mymethod(e)


# In[28]:

class Emp: # class 1 
    def __init__(self,id,name,salary):
        self.id = id # attribute
        self.name = name # attribute
        self.salary = salary # attribute
        
    def display(self): # method
        print ('Id=' , self.id)
        print ('Name=', self.name)
        print ('Salary= ', self.salary)
        
class Increment: # class 2 
    
    @staticmethod
    def mymethod(e):
        e.salary += 1000
        e.display()
    


# In[29]:

e = Emp(10,'Anuj Kumar',15000)


# In[30]:

Increment.mymethod(e)


# In[ ]:

# New employee

class Emp():
    pass

class DocumentVerification():
    pass


class OfferAcceptance():
    pass

class Onboarding():
    pass

class rollon_project():
    pass

class ethics_training():
    pass



# In[49]:

class Myclass:
    
    def __init__(self,x,n):
        self.x = x
        self.n = n
        
    @staticmethod
    def mymethod(x,n):
        result = x**n
        print ('{} to the power of {} is {}'.format(x,n,result))
        
    def modify(self):
        y = self.x + self.n
        print (y)


# In[34]:

Myclass.mymethod(5,3)


# In[35]:

Myclass.mymethod(5,4)


# In[51]:

object1.modify(5,6)


# In[52]:

# Inner class


# In[53]:

class Person():
    def __init__(self):
        self.name = 'Charles'
        self.db = self.Dob() # calling Dob object


# In[54]:

p = Person()
p.display()
print (p.name)
x = p.db
x.display()
print (x.yy)


# In[56]:

class Person():
    def __init__(self):
        self.name = 'Charles'
        self.db = self.Dob() # calling Dob object
        
    def display(self):
        print ('Name= ', self.name)
        
    # inner class
    
    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 1980
            
        def display(self):
            print ('Dob = {}/{}/{}'.format(self.dd, self.mm, self.yy))


# In[57]:

p = Person()


# In[58]:

p.display()


# In[59]:

x = p.db


# In[60]:

x.display()


# In[62]:

x = Person().Dob() # chaining


# In[63]:

x.display()


# In[64]:

p.display()


# In[65]:

# another version

class Person():
    def __init__(self):
        self.name = 'Charles'
        
    def display(self):
        print ('Name= ', self.name)
        
    # inner class
    
    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 1980
            
        def display(self):
            print ('Dob = {}/{}/{}'.format(self.dd, self.mm, self.yy))


# In[66]:

p = Person()


# In[67]:

p.display()


# In[68]:

x = Person().Dob()


# In[69]:

x.display()


# In[70]:

print (x.yy)


# In[ ]:



