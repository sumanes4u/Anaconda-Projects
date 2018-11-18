
# coding: utf-8

# In[1]:

import os


# In[2]:

os.getlogin()


# In[3]:

#os.getuid()


# In[4]:

import pwd


# In[5]:

pwd.getpwuid(os.getuid())


# In[6]:

os.getpid()


# In[7]:

os.getppid()


# In[8]:

os.getcwd()


# In[9]:

len(os.environ)


# In[10]:

os.environ['HOME']


# In[11]:

os.environ


# In[12]:

os.environ['testing123'] = '42'


# In[13]:

os.environ


# In[15]:

os.getcwd()


# In[16]:

#cd testdir/


# In[17]:

import subprocess as sub


# In[21]:

help(sub.call)


# In[22]:

sub.call(["ls", "-l"])


# In[23]:

import os


# In[24]:

os.listdir('.')


# In[25]:

os.stat('fileA.txt')


# In[ ]:

cwd = os.getcwd()
print (cwd)

os.listdir(cwd)
os.mkdir('test123')
os.listdir(cwd)
os.chdir('test123')
os.getcwd()

os.makedirs('abc/def/')


# In[27]:

import os,glob,shutil as sh


# In[47]:

os.listdir('.')


# In[29]:

glob.glob('*')


# In[30]:

glob.glob('*.txt')


# In[31]:

glob.glob('file*.txt')


# In[32]:

sh.copy('fileA.txt','fileX.txt')


# In[36]:

sh.copy('fileB.txt','subdir/fileY.txt')


# In[35]:

os.mkdir('subdir')


# In[39]:

os.listdir('subdir')


# In[38]:

sh.copytree('subdir','test3')


# In[41]:

sh.rmtree('test3')


# In[42]:

sh.move('subdir/fileY.txt','test4/fileZ.txt')


# In[46]:

os.listdir('test4')


# In[ ]:



