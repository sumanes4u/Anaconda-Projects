
# coding: utf-8

# In[1]:
'''
Data Types : 
    Numbers
    Strings
    Printing
    Lists
    Dictionaries
    Booleans
    Tuples
    Sets

Comparision Operators
if,elif, else statements
for Loops
while Loops
range() xrange()
list comprehension
functions
lambda expressions
map and filter
methods
classes.

'''
# In[2]:

# Arithmentics 


# In[3]:

print(1 + 1)


# In[4]:

print(1 * 3)


# In[5]:

print(1 / 2)


# In[6]:

print(2 ** 4)


# In[7]:

print(4 % 2)


# In[8]:

print(( 2 + 3) * ( 4 + 2))


# In[9]:

# Variable Assignments


# In[14]:

name1 = 'Ravi' # Variable name1, name2, values. 
name2 = 'Raj'


# In[15]:

name1 + " and "  + name2 + " are best friends" # Hard codes statements. 


# In[16]:

x = 1
y = 2
z = x + y
print(z)


# In[17]:

z


# In[18]:

# Strings and Integers or float numbers


# In[22]:

name = 'Raj'
age = 15
salary = 1.5


# In[20]:

type(name)


# In[21]:

type(age)


# In[23]:

type(salary)


# In[24]:

age + salary


# In[25]:

#age + name  ----> TypeError: unsupported operand type(s) for +: 'int' and 'str'


# In[30]:

name = int(input("What is your age "))


# In[31]:

age = 15


# In[32]:

type(age)


# In[34]:

age2 = str(age)


# In[35]:

type(age2)


# In[37]:

examplestr = "I am a good boy of age 14 and ears a salary of 1.5"


# In[38]:

type(examplestr)


# In[39]:

#int(examplestr)  --> alueError: invalid literal for int() with base 10: 'I am a good boy of age 14 and ears a salary of 1.5'


# In[40]:

# an int or float can be converter to string, and the revers is not possible. 


# In[49]:

print("This is an \"example\" of string")

print('This is an "example" of string')

print('I want to come at 6\'olock\'')


# Print statement


# In[57]:

x = "hello \"example\" "


# In[58]:

x


# In[59]:

print (x)


# In[61]:

print (x)


# In[62]:

# list 


# In[63]:

grocery = ['apple','mango','paste']


# In[71]:

for i in grocery:
    print (i,end='\n')


# In[69]:

type(grocery)


# In[70]:

grocery.append('soap')
print(grocery)

# In[72]:

grocery2 = ["rum","vodka"]
print(grocery2)

# In[73]:

finallist = grocery + grocery2


# In[74]:

print(finallist)


# In[76]:

hi = ['hey',2,[2,3]]


# In[77]:

hi[0]  # numbers are called index. 


# In[78]:

hi[1]


# In[80]:

hi[2]


# In[81]:

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


# In[82]:

list = [1,2,3,4]


# In[83]:

list


# In[86]:

dict = {'name1': 'Raj','age':'25'} # name-value pair


# In[87]:
print('DICTIONARY')
dict['name1']


# In[ ]:



