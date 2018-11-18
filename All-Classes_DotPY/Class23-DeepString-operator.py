
# coding: utf-8

# In[1]:

def reverse(input):
    n = len(input)
    x=""
    for i in range(n-1,-1,-1):
        x += input[i]
    return x


# In[2]:

reverse('12345')


# In[3]:

reverse(12345)


# In[4]:

a = 2


# In[5]:

len(a)


# In[6]:

a = '2'


# In[7]:

list = [1,2,3,4]


# In[8]:

list[-1]


# In[10]:

list[len(list)-1]


# In[11]:

list.pop()


# In[12]:

list


# In[13]:

import operator


# In[17]:

last = operator.itemgetter(-1)


# In[18]:

first = operator.itemgetter(0)


# In[19]:

last(list)


# In[20]:

first(list)


# In[21]:

list


# In[22]:

a = 5

print('The value of a is', a)
# Output: The value of a is 5

# The actual syntax of the print() function is :

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

# Output formatting

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

# Python Input

# input([prompt])

num = input('Enter a number: ')

print ( num )

# another format

num = int(input('Enter a number: '))

int('10')

float('10')


# In[23]:

name = 'John'


# In[24]:

age = '45'


# In[26]:

print ("I have a student, whose name is : " + name + ' and his age is : ' + age )


# In[32]:

a = '5'

print('The value of p is', a) # a could be of any type

print('The value of p is ' +  a) # a should be of string type


# In[ ]:

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


# In[33]:

print(1,2,3,4)


# In[35]:

print(1,2,3,4,sep=':')


# In[36]:

print(1,2,3,4,sep='#',end='&')


# In[37]:

x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))


# In[42]:

print('Hello {name}, {greeting}'.format(greeting = a, name = name)) # not to touch the print statement. 


# In[43]:

name


# In[44]:

name = input("Please enter your name : ")


# In[45]:

age = int(input("Please enter your age : "))


# In[46]:

type(name)


# In[54]:

a = list(range(0,10))


# In[53]:

a


# In[55]:

list = [1,2,3,4,5]


# In[ ]:




# In[56]:

def switch(argument):
    dict = {
        0:'zero',
        1:'one',
        2:'two',
    }
    
    return dict.get(argument,"nothing")


# In[57]:

switch(0)


# In[58]:

# do we've switch statement in python


# In[59]:

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
otherlist = [123, 'john']

print ( list )          # Prints complete list
print ( list[0] )       # Prints first element of the list
print ( list[1:3] )     # Prints elements starting from 2nd till 3rd
print ( list[2:] )      # Prints elements starting from 3rd element
print (list[::2]) #
print ( otherlist * 2 )  # Prints list two times
print ( list + otherlist ) # Prints concatenated lists
list.append(10)
print ( list )

list = ['larry', 'curly', 'moe']
list.append('shemp')  ## append elem at end
list.insert(0, 'xxx')  ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print ( list )  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print ( list.index('curly') )  ## 2

list.remove('curly')  ## search and remove that element
list.pop(1)  ## removes and returns 'larry'
print ( list )   ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']


# In[ ]:



