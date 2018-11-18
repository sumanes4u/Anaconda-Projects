
# coding: utf-8

# In[1]:

x = 'Hello'


# In[2]:

print(x)  # This print the value of the x as it gets stored


# print(x) # This prints the value in a suitable format. 

# In[3]:

num = 121
name = 'Sam'


# In[5]:

print('My number is:{one}, and my name is: {two}'.format(one=num,two=name))


# In[9]:

print('My number is:{}, and my name is: {}'.format(num,name))


# In[10]:

# List


# In[11]:

[1,2,3] # int


# In[12]:

['hi',1,2,3]  # int + string


# In[13]:

my_list = ['a','b','c']


# In[14]:

print(my_list.append('d'))


# In[15]:

print(my_list)


# In[16]:

print(my_list.pop())


# In[17]:

print(my_list)


# In[18]:

x = my_list.pop()


# In[19]:

print(x)


# In[20]:

l1 = [1,2,3]


# In[26]:

l2 = ['a','my basket','c']


# In[24]:

l3 = l1 + l2


# In[25]:

print(l3)


# In[27]:

print(my_list[0])


# In[28]:

print(my_list[1])


# In[29]:

#my_list[2] --> IndexError: list index out of range


# In[33]:

my_list = ['a','b','c','d','e','f']


# In[35]:

print(my_list[1:3])


# In[37]:

print(my_list[:4])


# In[40]:

print(my_list[2:-1])


# In[41]:

# Dictionaries


# In[42]:

d = {'key1':'value1','key2':'value2'}


# In[44]:

print(d['key1'])


# In[45]:

print(d.keys())


# In[46]:

print(d.values())


# In[47]:

print(d.items())


# In[48]:

print(my_list[0])


# In[49]:

my_list[0]='z'


# In[50]:

print(my_list[0])


# In[53]:

d['key3']='hello'


# In[54]:

print(d)


# In[55]:

# Booleans


# In[56]:

True


# In[57]:

False


# In[58]:

# Comparision Operator


# In[59]:

print(1 > 2)


# In[60]:

print(1 < 2)


# In[61]:

print(1 >= 1)


# In[62]:

print(1 <=4)


# In[63]:

print(1 == 1)


# In[64]:

print('hi' == 'hi')


# In[65]:

print('hi' == 'Hi')


# In[66]:

# Logical operator


# In[67]:

print(( 1 > 2) and ( 2 < 3))


# In[68]:

print(( 1 > 2) or ( 2 < 3))


# In[69]:

print(( 1 > 2) | ( 2 < 3))


# In[70]:

print(( 1 == 2) or (2 == 3) or (4 == 4))


# In[71]:

# List
# Dictionaries
# Tuples
# Sets


# In[73]:

#Tuples


# In[74]:

t = (1,2,3)


# In[75]:

print(t)


# In[76]:

#t[0] = 4  ---> TypeError: 'tuple' object does not support item assignment


# In[77]:

# Sets - removes duplicate


# In[78]:

{1,2,2,3,3,4,4,5,5}


# In[79]:

list = ['ravi','raj','ravi','priya','priya']


# In[80]:

another_list = set(list)


# In[81]:

print(another_list)


# In[82]:

another_list_set={1,2,2,3,3,}


# In[83]:

print(another_list_set)


# In[90]:

print(list[len(list)-1])


# In[89]:

list = ['ravi','raj','ravi','priya2']


# In[91]:

print(type(d))


# In[ ]:

#as


# In[ ]:




# In[ ]:



