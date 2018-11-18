
# coding: utf-8

# In[6]:

from operator import itemgetter
a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
#sorted(a)
#[(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
#sorted(a, key=itemgetter(0))
#[(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
#sorted(a, key=itemgetter(0, 1))
#[(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
#sorted(a, key=itemgetter(1))
#[(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
print(sorted(a, key=itemgetter(1), reverse=True))
#[(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]


# In[7]:

# sorting, really a complex operations. 


# In[8]:

a = [(5,3),(1,2)]


# In[9]:

print(sorted(a))


# In[11]:

print(sorted(a, key=itemgetter(1)))


# In[16]:

a = [(5,9),(8,2)]


# In[18]:

print(sorted(a, key=itemgetter(0)))


# In[19]:

a = [('Raj',50),('Arya',60)]


# In[20]:

print(sorted(a, key=itemgetter(0)))


# In[21]:

print(sorted(a, key=itemgetter(1)))


# In[22]:

a = [('Raj',50,'Europe'),('Arya',60,'China')]


# In[25]:

print(sorted(a, key=itemgetter(2)))


# In[26]:

a = [1,2,3,4,5]


# In[27]:

print(min(a))


# In[28]:

print(max(a))


# In[29]:

print(sum(a))


# In[43]:

a = '1,2,3,4,5 ' # How many elements are there ? 1


# In[44]:

print(a)


# In[45]:

print(len(a))


# In[32]:
a = [1, 2, 3]
print(sum(a))


# In[39]:

lista = [1,2,3,4,5] # How many elements are there ? len(<nameofthelist>)


# In[35]:

print(lista.insert(0,a))


# In[36]:

print(lista)


# In[38]:

print(len(lista))


# In[48]:

print(lista.extend(a)) # extend should be used for extending another list


# In[49]:

print(lista)


# In[50]:

lista = [1,2,3,4,5]


# In[51]:

lista.append(a)


# In[52]:

print(lista)


# In[58]:

print(lista[-1][-2])


# In[59]:

# diff between string vs list


# In[60]:

l1 = [1,2,3,4]


# In[63]:

l1[0]=9 # replaced 0 with 9


# In[64]:

print(l1)


# In[67]:

a = 'Hello' # immutable


# In[68]:

#a[0]='P' - TypeError: 'str' object does not support item assignment


# In[69]:

a.replace('H','P')


# In[70]:

print(a)


# In[71]:

print(id(a))


# In[75]:

a = a.replace('H','P') # Made a copy of a, replaced H with P, and then assigned it to a. 


# In[76]:

print(a)


# In[77]:

print(id(a))


# In[78]:

a = 1


# In[79]:

print(id(a))


# In[88]:

a = 2 # an object in memory with name as a 


# In[83]:

print(id(a))


# In[84]:

l1 = [1,2,3,4]


# In[85]:

print(id(l1))


# In[86]:

l1[0]=9


# In[87]:

print(id(l1))


# In[89]:

a = ["India","Japan","China"]


# In[90]:

print('India' in a)


# In[94]:

#list(range(10))  # one value: from 0 to value (excluded)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#list(range(3, 8))  # two values: from start to stop (excluded)
#[3, 4, 5, 6, 7]
print(list(range(-10, 10, 4)))  # three values: step is added
#[-10, -6, -2, 2, 6]


# In[95]:

# how do you do tuple unpacking


# In[106]:

list1 = ["Raj","Rachit"]


# In[107]:

a,b = list1


# In[109]:

print (a)


# In[110]:

print(list1[0])


# In[111]:

tup = ('Ravi','Rishi')


# In[112]:

d,e = tup


# In[113]:

print (d)


# In[99]:

from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print(vision[0])


# In[100]:

print(vision[1])


# In[101]:

print(vision.left)


# In[104]:

print(vision.right)


# In[115]:

exam = namedtuple('Student1', ['Science', 'Math'])


# In[119]:

result_student1 = exam(10,20)


# In[120]:

print(result_student1.Science)


# In[121]:

# swap
a, b = 1, 2
print("a is ", a)
print("b is ", b)
c = a  # we need three lines and a temporary var c
a = b
b = c
a, b  # a and b have been swapped
print("swapped")
print("a is ", a)
print("b is ", b)
#(2, 1)

# This is the standard method
print("Pythonic swap")
a, b = b, a  # this is the Pythonic way to do it
#a, b
(1, 2)


# In[ ]:



