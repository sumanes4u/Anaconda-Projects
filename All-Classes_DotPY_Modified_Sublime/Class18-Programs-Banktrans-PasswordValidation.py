
# coding: utf-8

# In[2]:

#1 convert input into output1 and output2

# input : 1,2,3,4

# output1 : [1,2,3,4]
# output2 : (1,2,3,4)

values = input("Enter seq of numbers like 1,2,3,4: ")
l = values.split(",")
t = tuple(l)
print (l)
print (t)


# In[10]:

test = 'hello how are you'
l = test.split(" ")
print(l)


# In[13]:

#2. 

a = "1:10,20,55,30,40"
# How do I get 10

print(a.split(":")[1].split(",")[0])


# In[21]:

#3. 

a = '123456789'

# How to reverse it. 

#a[start:end:step]
#a[0:5:3]

print(a[::-1])
#a[::1]


# In[22]:

# positive index : 0 1 2 3 4 5 6 7

# Negative index :          -3 -2  -1


# In[27]:

#4 

# Write a program that computes the net amount of a bank account based on transaction logs. 

#D 100
#W 50

netAmount = 0 

while True: # it will keep on asking you as long as you're going to provide an input
    s = input("enter number like D 100, W 50, blank to exit: ")
    if not s:
        break
    values = s.split() # capturing the input values
    operation = values[0] # one 
    amount = int(values[1]) # two
    if operation == 'D':
        netAmount += amount
    elif operation == 'W':
        netAmount -= amount
    else:
        pass
    print (netAmount)
    


# In[28]:

#5 

#You need to validate user passsword complexity. 

#1. At least 1 letter between [a-z]
#2. 1 upper case letter
#3. 1 number
#4. 1 character ( $#@)
#5. min length : 6
#6. max length : 12
#7. should not have space
                
# input a list of passwords, and accept only those which matches your complexity criteria
                



# In[ ]:

import re
value = []
items = [x for x in input("Enter a word for password: ").split(',')] # list comprehension 

for p in items:
    if len(p) < 6 or len(p) > 12:
        print("Password length should be between 6 and 12")
        continue
    else:
        pass
    if not re.search("[a-z]",p): # abcdefghij.....z
        print("There is no lower case present")
        continue
    elif not re.search("[A-Z]",p): # ABCDEF
        print("There is no upper case letters")
        continue
    elif not re.search("[0-9]",p): # 012345689
        print("There are no numbers")
        continue
    elif not re.search("[$#@]",p): # $#@
        print("There are no special characters [$#@]")
        continue
    elif re.search("\s",p):
        print("There is no space")
        continue
    else:
        pass
    value.append(p)
print (",".join(value))


# In[ ]:



