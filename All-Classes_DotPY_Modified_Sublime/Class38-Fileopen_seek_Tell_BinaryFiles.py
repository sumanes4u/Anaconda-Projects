
# coding: utf-8

# In[1]:

# Seek() and Tell()


# In[3]:

# n = f.tell() # tell tells us the position of the cursor. n is the integer position. 


# In[ ]:

#f.seek(offset,fromwhere), f.seek(10,0)


# In[8]:

with open('line.txt','w+b') as f:
    f.write(b'Amazing Python')


# In[6]:

#pwd


# In[ ]:

#Amazing Python


# In[ ]:

1234567891011121314


# In[10]:

f = open('line.txt','r')


# In[11]:

f.seek(3) # This will put the file pointer at 3+1 = 4th position. 


# In[12]:

print(f.read(2))


# In[13]:

print (f.tell())


# In[15]:

f.seek(-1) # pointer to the 5th position ( -6 +1 = 5)


# In[16]:

f.close()


# In[17]:

f = open('line.txt','rb')


# In[18]:

f.seek(-1,2)


# In[19]:

f.close()


# In[20]:

f = open('line.txt','rb')


# In[21]:

f.seek(3)


# In[22]:

print(f.read(2))


# In[23]:

print (f.tell())


# In[25]:

f.seek(-6,2)


# In[26]:

f.read(1)


# In[27]:

f.tell()


# In[28]:

# f.seek(offset,fromwhere)


# In[ ]:

f.read(10)


# In[29]:

f.close()


# In[31]:

str = 'Dear'
with open('data.bin','wb') as f:
    f.write(str.encode())   # convert str into byte
    f.write(b'Hello')


# In[32]:

# example to store file in binary format. 

reclen = 20 # record length

with open("cities.bin",'wb') as f:
    n = int(input('How many entries? '))
    
    for i in range(n):
        city = input('Enter city name: ')
        ln = len(city)
        
        # increase the city name to 20 characters
        
        city = city + (reclen-ln)*' '
        
        city = city.encode()
        
        f.write(city)


# In[34]:

reclen = 20


# In[35]:

f = open("cities.bin", 'rb')


# In[37]:

f.seek(reclen * 2)


# In[38]:

f.read()


# In[39]:

f.close()


# In[42]:

import os

reclen = 20

size = os.path.getsize('cities.bin')
print ('Size of the file = {} byes'.format(size))

n = int(size/reclen)
print ('NO of records = {}'.format(n))

with open('cities.bin','r+b') as f: 
    name = input('Enter City name: ')
    name = name.encode()
    newname = input('Enter new name: ')
    
    ln = len(newname)
    
    newname = newname + (20-ln) * ' '
    
    newname = newname.encode()
    
    position = 0
    
    found = False # find it change to True, else it will remain as False
    
    for i in range(n):
        f.seek(position)
        
        str = f.read(20)
        
        if name in str:
            print ('Updated record no: ', (i+1))
            found = True
            
            # go back 20 bytes from current position
            f.seek(-20,1)
            
            # update the record
            f.write(newname)
            
        position += reclen
        
    if not found :
        print ('City not found')


# In[43]:

# Zipping and Unzipping files


# In[44]:

# f = ZipFile('test.zip','w',ZIP_DEFLATED)


# In[45]:

from zipfile import *


# In[46]:

dir()


# In[47]:

# creating a zipfile 

f = ZipFile('test.zip','w',ZIP_DEFLATED)
# add some files. these are going to be zipped

f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')

print ('test.zip file created.....')
f.close()


# In[48]:

z = ZipFile('test.zip','r')


# In[49]:

names = z.namelist()


# In[51]:

names


# In[50]:

f = z.open(file1.txt)


# In[ ]:

contents = f.read()
print (contents.decode())


# In[52]:

# Working with Directories. 


# In[53]:

pwd


# In[54]:

import os


# In[55]:

os.getcwd()


# In[56]:

os.mkdir('mysubdir')


# In[57]:

os.mkdir('mysubdir/mysub2')


# In[58]:

os.chdir('mysubdir/mysub2/')


# In[59]:

os.getcwd()


# In[60]:

os.chdir('/Users/aws/mysubdir')


# In[61]:

os.getcwd()


# In[62]:

os.rmdir('mysub2')


# In[63]:

pwd


# In[66]:

os.makedirs('mysub/mysub2/mysub3')


# In[67]:

os.removedirs('mysub/mysub2/mysub3')


# In[68]:

os.mkdir('mysub')


# In[69]:

os.rename('mysub','newsub')


# In[70]:

#os.walk(path,topdown=True,onerror=None,followlinks=False)


# In[75]:

import os
for dirpath,dirnames,filenames in os.walk('.'):
    print ('Current path: ', dirpath)
    print ('Directories: ', dirnames)
    print ('Files: ', filenames)
    print ()


# In[72]:

pwd


# In[76]:

ls


# In[78]:

os.system('ls -ltrh')


# In[80]:

os.system('demo.py') # run demo.py program


# In[81]:

ls 


# In[82]:

os.system('ls')


# In[83]:

help(os.system)


# In[84]:

help(os.mkdir)


# In[ ]:

#read(4),write(2),execute(1) = 7
#ugo = user,group,others.


# In[ ]:

# arrays - list 

