
# coding: utf-8

# In[1]:

# Iterators

# Iterators are objects that can be iterated upon. ( __iter__) and (__next__)

# list, tuple, string are iterables. 

# The iter() function ( which in turn calls the __iter__() method) returns an iterator 
# from them. 



# In[2]:

list = [1,2,3,4]

# get an iterator using iter()

my_iter = iter(list)

# iterate
# next(obj)

# 1
print (next(my_iter))

# 2
print (next(my_iter))

#3
print (my_iter.__next__())

#4
print (my_iter.__next__())

# nothing is there. 
next(my_iter) # raise an error. 



# In[3]:

list2 = [2,4]

list_obj = iter(list2)


# In[5]:

for element in list:
    print (element)


# In[6]:

# create an iterator object from that iterable

iter_obj = iter(list)

while True:
    try:
        # get the next item
        element = next(iter_obj)
        
    except StopIteration:
        break


# In[47]:

class example:
    try:
        
        def __init__(self,max = 0):
            self.max = max
    
        def __iter__(self):
            self.n = 0
            return self
    
        def __next__(self):
            if self.n <= self.max:
                result = 2 ** self.n
                self.n += 1
                return result
            else:
                raise StopIteration
    except StopIteration :
        print ("nothing is there")
        


# In[48]:

a = example(4)


# In[49]:

i = iter(a)


# In[50]:

next(i)


# In[51]:

next(i)


# In[52]:

next(i)


# In[53]:

next(i)


# In[54]:

next(i)


# In[55]:

next(i)


# In[56]:

# Generator

def my_gen():
    n = 1
    print ("This is printed first")
    # Generator function contains yield statements
    yield n
    
    n += 1
    print ('This is printed second')
    yield n
    
    n += 1
    print ('This is printed at last')
    yield n


# In[57]:

a = my_gen()


# In[58]:

next(a)


# In[59]:

next(a)


# In[60]:

next(a)


# In[61]:

next(a)


# In[ ]:



