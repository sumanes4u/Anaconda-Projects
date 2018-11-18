
# coding: utf-8

# In[11]:

# creating a workflow. 

# how do you create a function. 

# involving loop

# involving module. 

# what is a method

def walk(bal1=0,bal2=0): # inp1 and inp2 are input parameters.
    print ("To Walk......")
    print (bal1)
    print (bal2)


# In[12]:

walk(5,6)


# In[ ]:

import random

def main():
    # Initialize the program
    print ('Guess a number between 1 and 100')
    
    
    #randomNumber = 40
    randomNumber = random.randint(1,100)
    # flag 
    found = False
    
    while not found: # run this loop as long as found is set to false
        userGuess = int(input("Your guess:  "))
        
        if userGuess == randomNumber:
            print ("You have got it")
            found = True
        elif userGuess > randomNumber:
            print ("Guess lower")
        else:
            print ("Guess Higher")   
    
    # __ ( double underscore, dunder )
if __name__ == "__main__":
    main()


# In[24]:

import random


# In[28]:

random.randint(1,10)


# In[35]:

list = [1,2,3,4]


# In[36]:

list2 = ['one','two','three','four']


# In[37]:

print(list)


# In[38]:

print(list2)


# In[39]:

list.append(5)


# In[40]:

print(list)


# In[41]:

list2.append('five')


# In[42]:

print(list2)


# In[43]:

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the 
# sentence capitalized. 


# In[46]:

lines = [] # empty list
while True:
    s = input("Enter sequence of lines:")
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print (sentence)


# In[47]:

print(list2)


# In[48]:

s = list2


# In[49]:

print(s)


# In[52]:

for item in list2:
    print (item.upper())


# In[54]:

list3 = [element.upper() for element in list2] # list comprehension


# In[55]:

print(list3)


# In[ ]:



