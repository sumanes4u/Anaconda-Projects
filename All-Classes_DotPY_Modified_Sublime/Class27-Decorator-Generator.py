
# coding: utf-8

# In[1]:

max = lambda x,y:x if x>y else y


# In[3]:

max(5,6)


# In[5]:

def func(n):
    i = 0
    while i < n:
        print ('The count is:', i)
        i += 1


# In[10]:

a = lambda x: func(x) # Anonymous function


# In[11]:

a(5)


# In[12]:

func(5)


# In[16]:

def func(arguments): # func is the name of this function
    return expression


# In[17]:

name = lambda arguments: expression # anonymous


# In[19]:

def func(n):
    print ('The count is :', n)


# In[20]:

a = lambda funcParam, count : (funcParam(i) for i in range(count))


# In[21]:

a(func,5)


# In[22]:

# Decorator


# In[34]:

#1
def decor(fun): # fun should be a function
    def inner():
        value = fun() # access value returned by fun
        return value + 2 # increase the value by 2 
    return inner


# In[26]:

def num():
    return 10


# In[27]:

result_fun = decor(num)


# In[29]:

result_fun()


# In[30]:

# How do we use decor function
@decor
def num():
    return 10


# In[31]:

print (num())


# In[32]:

@decor
def num2():
    return 20


# In[33]:

print (num2())


# In[35]:

#2
def decor(fun): # fun should be a function
    def inner():
        value = fun() # access value returned by fun
        return value + 2 # increase the value by 2 
    return inner

def decor1(fun): # fun should be a function
    def inner():
        value = fun() # access value returned by fun
        return value * 2 # increase the value by 2 
    return inner

def num():
    return 10

result_fun = decor(decor1(num)) # easier to understand
print (result_fun())


# In[36]:

@decor
@decor1 # nearest one will execute first
def num():
    return 10


# In[37]:

print (num())


# In[38]:

# Generators


# In[39]:

# Generators are functions that return a sequence of values. 


# In[40]:

def mygen(x,y):
    while x <= y: # this is loop repeats from x to y, and keeps checking if x is less or equal y
        yield x # return x value
        x += 1 # increment x value by 1 


# In[57]:

g = mygen(5,10) # g will be a sequence, mygen will return a generator object because of yield statement. 


# In[58]:

for i in g:
    print (i, end=' ')


# In[59]:

g


# In[63]:

#del list


# In[64]:

list1 = list(g)


# In[65]:

#list1(g)
# In[77]:

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'


# In[78]:

g = mygen()


# In[79]:

type(g)


# In[70]:

def mygen1():
    print ('hi')


# In[71]:

type(mygen1)


# In[80]:

print (next(g)) # A
print (next(g)) # B
print (next(g)) # C
print (next(g)) # Nothin is there to pop. 


# In[82]:

lst = [1,2,3,4]


# In[83]:

next(lst)


# In[84]:

# Is list an interator : 'list' object is not an iterator


# In[85]:

lst


# In[87]:

type(lst)


# In[86]:

for number in lst:
    print (number.next())


# In[88]:

# List is iterable, but they are not iterators. 


# In[105]:

lst


# In[106]:

it = iter(lst)


# In[107]:

type(it)


# In[108]:

for i in it:
    it.next()
    print (i)


# In[109]:

for i in it:
    it.__next__()
    print (i)



# In[110]:

def da(basic):
    da = basic*80/100
    return da

def hra(basic):
    hra = basic*15/100
    return hra
    
def pf(basic):
    pf = basic*12/100
    return pf

def itax(gross): # tax payable
    tax = gross*0.1
    return tax

basic = float(input('Enter basic salary: '))

gross = basic + da(basic) + hra(basic)
print ('Your gross salary: {:10.2f}'.format(gross))

net = gross - pf(basic) - itax(gross)
print ('Your net salary: {:10.2f}'.format(net))


# In[ ]:



