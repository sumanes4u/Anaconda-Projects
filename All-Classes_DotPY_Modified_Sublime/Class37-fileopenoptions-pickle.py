
# coding: utf-8

# In[1]:

# Types of Files in Python

# Text File
# Binary File


# In[ ]:

# opening a file

#file_handler = open('filename','open mode',"buffering")


# In[ ]:

# different types of mode
'''
w = write
r = read
a = append, if the file does not exist, then it will create a new file. 
w+ = write and read data of a file. The previous data in the file will be deleted. 
r+ = read and write data into a file. The previous data in the file will not be deleted.
a+ = To append and read data of a file. The file pointer will be at the end of the file if the file exists.
If the file does not exist, it creates a new file for reading and writing.
x = to open the file in exclussive creation mode. 

'''
# In[5]:

# open a file
f = open('myfile.txt',"w")

# Write something over the file
f.write('I am good')

# close a file
f.close()


# In[14]:

f3 = open('myfile3.txt')


# In[15]:

f3.close()


# In[16]:

f1 = open('myfile.txt',"w")

str = input('Enter text: \n')

f1.write(str)

f1.close


# In[19]:

f1 = open('myfile.txt',"r")

str = f1.read()

# display

print (str)

f1.close()


# In[20]:

f = open('myfile.txt', 'w')

print ('Enter text (@ at the end): ')

while str != '@':
    str = input()
    if (str !='@'):
        f.write(str + "\n")
        
f.close()


# In[ ]:

f.read()
#This is my file line 
#This is line two


# In[ ]:

f.readlines()

['This is my file line.\n', 'This is line two.\n']


# In[ ]:

f.read().splitlines()


# In[ ]:

['This is my file line.', 'This is line two.']


# In[21]:

f = open('myfile.txt','r')

print ('The file contens are: ')

str = f.read() # 1

print (str)

f.close()


# In[23]:

f = open('myfile.txt','r')

print ('The file contens are: ')

str = f.readlines() # 2 

print (str)

f.close()


# In[26]:

f = open('myfile.txt','r')

print ('The file contens are: ')

str = f.read().splitlines()# 2 

print (str)

f.close()


# In[27]:

f = open('myfile.txt','r')


# In[28]:

f.close()


# In[ ]:

# f.seek(offset,fromwhere)
# offset represent, how many bytes to move. fromwhere - represent from which position to move. 

f.seek(10,0)

#o , represent from the beginning of the file, 1 represent from the current position in the file, 
#and 2 rep end of the file.


# In[33]:

f = open('myfile.txt', 'a+')

print ('Enter text (@ at the end): ')

while str != '@':
    str = input()
    if (str !='@'):
        f.write(str + "\n")
        
f.seek(0,0)

print ('The file contens are : ')

str = f.read()
print (str)
f.close()


# In[30]:

f.close()


# In[40]:

f = open('myfile.txt', 'a+')

f.seek(0,0)

str = f.read()
print (str)
f.close()


# In[45]:

f = open('myfile.txt', 'a+')

f.seek(5,0)

str = f.read()
print (str)
f.close()


# In[46]:

import os


# In[47]:

# where a file exists or not. 


# In[ ]:

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname + 'does not exist')
    sys.exit() # terminate the program


# In[50]:

import os,sys

fname = input('Enter filenname: ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname + ' does not exist')
    sys.exit() # terminate the program
    
# read strings from the file
print ('The file contents are : ')

str = f.read()
print (str)

f.close()


# In[ ]:

for line in f:
    print (line)


# In[ ]:

for line in f:
    print (line)
    words = line.split()
    print (words)


# In[ ]:

for line in f:
    print (line)
    words = line.split()
    print (words)
    c1 += 1 
    cw += len(words)
    cc += len(line)


# In[51]:

import os,sys
fname = input('Enter filename: ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print (fname = ' does not exist')
    sys.exit()

# counters
cl = cw = cc = 0

for line in f:
    words = line.split()
    cl += 1
    cw += len(words)
    cc += len(line)
    
print ('No of lines: ', cl)
print ('No of words: ', cw)
print ('No of characters: ',cc )

f.close()


# In[52]:

# Working with Binary files. 


# In[53]:

f1 = open('cat.jpeg', 'rb')
f2 = open('new.jpeg','wb')

bytes = f1.read()
f2.write(bytes)

f1.close()
f2.close()


# In[54]:

pwd


# In[ ]:

f1 = open('c:\\asdf\\asdfas\\cat.jpeg')


# In[61]:

# with 
# with open('filename','openmode') as fileobject

with open('sample.txt','a') as f : 
    f.write('I am a another learner\n')
    f.write('I am a another python learner\n')


# In[63]:

with open('sample.txt','r') as f : 
    for line in f:
        print (line)


# In[64]:

# pickle


# In[70]:

class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
        
    def display(self):
        print ("{:5d} {:20s} {:10.2f}".format(self.id,self.name,self.sal))


# In[71]:

raj = Emp(33,'Raj',5000)


# In[72]:

raj.display()


# In[73]:

# serialization

# converting a class object into a byte of stream so that it can be stored in a file. 


# In[ ]:

# pickle.dump(object,file)

# object = pickle.load(file)


# In[74]:

import pickle


# In[76]:

pickle.dump(raj,'fileraj')


# In[79]:

import pickle

a = ['test value','test value 2','test value 3']
a
['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)   

# here we close the fileObject
fileObject.close()


# In[2]:

with open('tmpfile','w') as f:
    str = ''
    while str != '@':
        str = input('')
        if str != '@':
            f.write(str+'\n')
        else:
            break    


# In[9]:

#bubble sort algorithm
from array import *
arry1 = array('i',[])

num = int(input('Enter number of elements'))
for i in list(range(num)):
    elm = int(input('Enter element:'))
    arry1.append(elm)
print (arry1)  
ln = len(arry1)
print ('Array length is:{length}'.format(length=ln))
for i in list(range(ln)):


# In[5]:

    arry1.append(10)


# In[6]:

arry1.append(20)


# In[7]:

arry1


# In[ ]:



