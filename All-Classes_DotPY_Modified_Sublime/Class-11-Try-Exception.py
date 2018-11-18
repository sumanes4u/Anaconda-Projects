
# coding: utf-8

# In[41]:

# try ( exception may occur)  > raise ( Raise an exception ) 
#                                                          > except ( catch if exception occurs)


# In[ ]:

import sys

randomList = ['a',0,2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print ('Oops!',sys.exc_info()[0],"occured")
        print("Next Entry")
        print()
print("The reciprocal of",entry,"is",r)


# try:
#     a = int(input('Enter number '))
#     b = int(input('Enter another number '))
#     
#     c = a/b 
#     print(c)
# except ZeroDivisionError as e:
#     print('Some exceptional situation occurred!',e,e.__class__.__name__)
#     
# print('some other task continues here')

# # A try clause can have any number of except clause to handle them differently but only one will 
# # executed in case of an exception occurs. 
# try:
#     # do something
#     pass
# except ValueError:
#     # handle ValueError exception
#     pass
# except (TypeError, ZeroDivisionError):
#     # handle multiple exceptions
#     # TypeError and ZeroDivisionError
#     pass
# except:
#     # handle all other exceptions
#     pass
# 
# 

# In[ ]:

# Raising Exceptions


# In[ ]:

##raise KeyboardInterrupt


# In[ ]:

##raise MemoryError("this is an argument")


# In[ ]:

try:
    a = int(input("Enter a positive interger: "))
    if a <= 0: 
        raise ValueError("That is not a positive number!")
    else:
        print ('Positive Number')
except ValueError as ve:
    print (ve)


# In[ ]:

# try..finally , if, elif, elif, else
try: 
    f = open("test.txt", encoding = 'utf-8')
    # perform file operation
except: 
    print ('abc')
finally:
    print ('FINALLY')
#    f.close()


# In[ ]:

while True:
    try:
        names = ['Vivek','Suman','Sahil']
        print (names)
        name = input('Enter name : ')
        
        if name in names:
            print('Welcome ' + name + '!!!')
            break;
        else:
            raise Exception('name not found in list')
    except Exception as e:
        print ('some unknown exception occured',e,e.__class__.__name__)
        print ('some unknown exception occured')
    finally:
        print ('finally block always executes')
            
            


# In[27]:

print(locals()['__builtins__'])


# In[ ]:

try:
    a = int(input('Enter number '))
    b = int(input('Enter another number '))
    
    c = int(a/b) 
    print(c)

except ZeroDivisionError as e:
    print('Some exceptional situation occurred!',e,e.__class__.__name__)
except Exception as e: # parent class handler can handle any child error.
    print ('some exception occurred',e,e.__class__.__name__)
    
print('some other task continues here')


# In[32]:

#*args vs **args
def func(input1,input2):
    print (input1)
    print (input2)


# In[34]:
##Below throws an error as the above func can take only 2 arguments 
##func('a','b','c')


# In[44]:

#*args vs **args
def func(*args):
    for a in args:
        print (a)
    


# In[45]:

func('a','b','c')


# In[51]:

def func_dict(**kwargs):
    for a in kwargs:
        print ( a, kwargs[a])


# In[52]:

func_dict(name='one',age=27)


# In[48]:
##Below throws error - TypeError: func() got an unexpected keyword argument 'name'
##func(name='one',age=27)


# In[49]:

class CustomError(Exception):
    pass


# In[51]:

#raise CustomError("This is my custom error")


# In[ ]:

class NameNotFound(Exception): # NameNotFound is a class which inherits from the Exception
    def __init__(self,msg='Name not found in the List!'):
        super().__init__(msg)
        
while True: 
    try:
        names = ['Vivek','Suman','Sahil']
        print (names + list('try another name not in the list for custom exception to occur'))
        name = input('Enter name: ')
        
        if name in names:
            print('Welcome ' + name + '!!!')
            break;
        else:
            raise NameNotFound
    except NameNotFound as e:
        print(e)
    except Exception as e:
        print('Some unknown exception: ', e)


# In[57]:

class ValueTooSmallError(Exception):
    """ Raised when the input value is too small"""
    pass

class ValueTooLargeError(Exception):
    """Raised when the input value is too large"""
    pass

number = 10

while True:
    try: 
        
        num = int(input('Enter a number: '))
        if num < number:
            raise ValueTooSmallError
        elif num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print ('This value is too small, try again!')
        print()
    except ValueTooLargeError:
        print ('This value is too large,try again!')
        print()
print("Congratulations! You guessed it correctly")


# In[ ]:



