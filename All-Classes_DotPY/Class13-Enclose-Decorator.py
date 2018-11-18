
# coding: utf-8

# In[1]:

# closure

# closure = function()


# In[6]:

def print_msg(msg):
    
    def printer():
        print(msg)
        
    printer() # Printer() was able to access the non-local variable msg of the enclosing func.


# In[7]:

print_msg('Hello')


# In[8]:

#2. 

def print_msg(msg):
    
    def printer():
        print(msg)
        
        
    return printer()


# In[9]:

another = print_msg("Hello")
# attribute = function 


# In[10]:

print (another)


# In[11]:

another()


# In[12]:

del print_msg


# In[13]:

another()


# In[13]:

print_msg("Hello")


# In[15]:

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)

times5 = make_multiplier_of(5)

print(times3(9))

print(times5(3))

print(times5(times3(2)))


# In[16]:

# decorators


# In[16]:

def first(msg):
    print(msg)
    
first("Hello")

second = first
second("Hello")


# In[17]:

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func,x):
    #result = func(x)
    return func(x)


# In[18]:

operate(inc,3)


# In[19]:

operate(dec,3)


# In[18]:

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print ("I a ordinary")


# In[19]:

ordinary()


# In[20]:

pretty=make_pretty(ordinary)


# In[21]:

pretty()


# In[34]:

# Decorator. 
@make_pretty
def ordinary():
    print ("I am ordinary")


# In[35]:

ordinary()


# In[37]:

def make_pretty1():
    def inner():
        print("I got decorated")
        func1()
    return inner


# In[38]:

@make_pretty1
def ordinary():
    print ("I am ordinary")
ordinary()    


# In[59]:

def packing_ka(func):
    print ("10")
    #func
    return func()
    
def packing_tn(func):
    print ("8")
    #func
    return func()
    
@packing_ka
def make_buscuit1():
    print("buscuit-ka")


@packing_tn
def make_buscuit2():
    print ("buscuit-tn")





# In[60]:

def smart_divide(func):
    def inner(a,b):
        print("I am going to divide")
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a,b)
    return inner
    


# In[63]:

@smart_divide
def divide(a,b):
    return (a/b)


# In[64]:

divide(2,5) #- work
divide(2,0) #- not work


# In[54]:

def divide(a,b):
    return (a/b)


# In[ ]:



