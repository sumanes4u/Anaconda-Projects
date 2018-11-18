
# coding: utf-8

# In[ ]:

# Global and Local Variables 


# In[1]:

#1
# This function uses global variable s

def f():
    print (s)
    
# Global scope

s = 'I am a good boy'
f()


# In[2]:

#2

# This function has a variable with name same as s.

def f():
    s = "Mee too"
    print (s)
    
# Global Scope
s = 'I am a good boy'
f()
print(s)


# In[7]:

# 3. 


# This function has a variable with name same as s.

def f():
    print (s)
    s = "Mee too"
    print (s)
    
# Global Scope
s = 'I am a good boy'
f()
print(s)


# In[8]:

# 4. To make the above program work. 

def f():
    global s
    print (s)
    s = "Mee too"
    print (s)
    
# Global Scope
s = 'I am a good boy'
f()
print(s)


# In[3]:

#5.
a = 1
# Uses global because there is no local 'a'
def f():
    print ('Inside f(): ', a )
# Variable 'a' is redefined as a local
def g():
    a = 2
    print ('Inside g() : ' , a )    
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print ('Inside h() : ', a)
def i():
    global a
    a = 5
    print ('Inside i() : ', a)
    # Since you make a variable as global, hence the value is carried globally(outside the func)
# Global scope
print ('global : ', a)
f()
print ('global : ', a )
g()
print ('global : ', a )
h()
print ('global : ', a )
print (a)
i()
print ('global : ', a )
print (a)    


# In[1]:

import getpass


# In[ ]:

getpass.

