
# coding: utf-8

# In[9]:

class emp_raise(object):
    hike = 5  #variable of a class
    
    def __init__(self,first_name,last_name,pay):
        self.first = first_name
        self.last = last_name
        self.pay = pay
        self.email = first_name + last_name + '@' + 'cisco.com'
        
    def raise1(self):
        self.pay = int(self.pay * emp_raise.hike)
        return(self.pay)
        
print ("All employees are eligible to get %d percentHIKE:"%(emp_raise.hike))
    
emp1 = emp_raise('suman','samarthi',1000)
print (emp1.pay)
emp1.raise1()
print (emp1.pay)
  
    


# In[10]:

class pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)
    
dough = pet("nimmy","dog")

class cat(pet):
    def __init__(self,name,hate_dogs):
        pet.__init__(self,name,"cat")
        self.hate_dogs = hate_dogs
    def cuts(self):
        return "%s really HATE DOGS:%s"%(self.name,self.hate_dogs)
t1 = cat("cuttie","Yes")


# In[11]:

print(t1.hate_dogs)


# In[12]:

print(t1.cuts())


# In[13]:

class salHike(object):
    Hike = 5  #varilable or attribute 
    
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@" + "hp.com"
        
    def email(self):
        return first + "." + last + "@" + "hp.com"
        
    def increase(self):
        self.salary = int(self.salary * salHike.Hike)
        return (self.salary)
        
Suman = salHike("suman","samarthi",10000)        
print ("The minimun Hike is %d"%Suman.Hike)
print ("The current Sal for %s is:%d"%(Suman.first,Suman.salary))
Suman.increase()
print ("The increment sal for %s is %d"%(Suman.first,Suman.salary))


Pranav = salHike("pranav","damala",20000)
print ("The current Sal for %s is:%d"%(Pranav.first,Pranav.salary))
Pranav.increase()
print ("The incremented salf for %s is %d"%(Pranav.first,Pranav.salary))


# In[28]:

class customer(object):
    def __init__(self,name):
        self.name = name
    def set_balance(self,balance=0.0):
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise RuntimeError('Amount is greater that Balance')
        self.balance -= amount
        return self.balance
    def deposite(self,amount):
        self.balance += amount
        return self.balance
suman = customer('pranav')      


# In[29]:

suman.set_balance(1000)


# In[30]:

suman.withdraw(100)


# In[31]:

suman.deposite(100)


# In[32]:

suman.withdraw(2000)


# In[ ]:



