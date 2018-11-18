
# coding: utf-8

# In[13]:

list = [1,2,3,4]

for i in list[0:len(list)]:
    print (i)


# In[4]:

list[-1]


# In[5]:

# splice


# In[8]:

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
otherlist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (otherlist * 2)  # Prints list two times
print (list + otherlist) # Prints concatenated lists
list.append(10)
print (list)


# In[14]:

# list - list = [1,2,3,4] or ['a','b','hi'] or [1,2,'hi']
# tuple - (1,2,3,4), list vs tuple - tuple is immutable, it is read only. 
# dictionaries - {'key1':'value1','key2':'value2'}
# set - {1,1,2,3,3,3}, removes the duplicates. 


# In[23]:

list1 = [1,2,3,4]


# In[24]:

list2 = ['hi','a',1]


# In[16]:

# append vs extend


# In[25]:

list1.append([1,2,3,4])


# In[26]:

list1


# In[30]:

list1[-1]


# In[31]:

list2.extend([1,2,3])


# In[32]:

list2


# In[33]:

list2[-1]


# In[34]:

tuple1 = (1,2,3,4)


# In[35]:

tuple1[1]=5


# In[36]:

duplicate_list = [1,1,'ravi','ravi','suman','suman']


# In[44]:

unique_list = list(set(duplicate_list))


# In[38]:

unique_list


# In[42]:

new_unique_list = list(unique_list)


# In[43]:

type(new_unique_list)


# In[45]:

# Loops


# In[47]:

if 1 < 2: # We dont use braces in python, we use indent
    print('Yep!')


# In[48]:

if 1 < 2: # condition
    print('first') # statements
    # do something
else:
    print('second')


# In[49]:

if 1 > 2: # condition
    print('first') # statements
    # do something
else:
    print('second')


# In[52]:

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
elif 3 == 3:
    print ('next middle')
else:
    print ('Last')


# In[53]:

# for loops


# In[54]:

list = [1,2,3,4]


# In[58]:

for i in list:
    print(i,end='\t')


# In[59]:

for i in list:
    print('yep')


# In[63]:

for i in list:
    if i < 3:
        print(i+i)


# In[61]:

# while loops


# In[62]:

i = 1
while i < 5 :
    print('i is : {}'.format(i))
    i = i +1


# In[64]:

range(5)


# In[65]:

for i in range(5):
    print(i)


# In[66]:

list(range(5))


# In[70]:

list(range(5))


# In[68]:

list


# In[71]:

another = list(range(5))


# In[74]:

type(list3)


# In[75]:

l1 = [1,2,3]


# In[76]:

type(l1)


# In[79]:

t = (1,2,3)


# In[80]:

type(t)


# In[81]:

# break and continue


# In[82]:

for val in "string":
    if val == 'i':
        break # it ends the loop
    print(val)
print("the end")


# In[83]:

for val in "string":
    if val == 'i':
        continue # it ends the iteration
    print(val)
print("the end")


# In[88]:

for val in list:
    if val == '1':
        break # it ends the loop
    print(val)
print("the end")


# In[86]:

list = [1,2,3,4]


# In[87]:

list


# In[91]:

for val in list:
    if val == 1:
        continue # it ends the loop
    print(val)
print("the end")


# In[92]:

# switch loop ( not there in python)


# In[102]:

def f(x):
    return {
        1 : 'dosa',
        2 :'tea',
    }[x]


# In[103]:

f(1)


# In[99]:

d = {1:'dosa',
     2:'tea'}


# In[ ]:



