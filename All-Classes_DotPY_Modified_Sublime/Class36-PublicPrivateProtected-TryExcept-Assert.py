
# coding: utf-8

# In[1]:

# Public, private, protected


# In[9]:

class Myclass:
    
    def __init__(self,name,surname,salary):
        self.name = name # Public
        self.surname = surname
        self.salary = salary
        
    def test(self):
        print (self.name)
        print (self.surname)
        print (self.salary)
        


# In[10]:

obj = Myclass('Raj','Kumar',5000)


# In[5]:

obj.name


# In[6]:

obj.salary


# In[7]:

obj.surname


# In[11]:

obj.test()


# In[12]:

class Myclass2:
    
    def __init__(self,name,surname,salary):
        self.name = name # Public
        self._surname = surname # Protected
        self.__salary = salary # Private 
        
    def test(self):
        print (self.name)
        print (self.surname)
        print (self.salary)


# In[14]:

obj = Myclass2('Raj','Kumar',5000)


# In[57]:

obj._surname


# In[16]:

obj._Myclass2__salary


# In[56]:

# Security, it buy deception, hiding. and by protection. 


# In[26]:

class Cup:
    def __init__(self):
        self.color = None
        self.content = None
        
    def fill(self,beverage):
        self.content = beverage
        
    def empty(self):
        self.content = None


# In[27]:

redCup = Cup()


# In[20]:

redCup.color = 'red'


# In[21]:

redCup.content = 'tea'


# In[22]:

redCup.empty()


# In[23]:

redCup.content


# In[34]:

redCup.fill("tea")


# In[35]:

redCup.content


# In[36]:

redCup.empty()


# In[37]:

# Protected


# In[38]:

class Cup:
    def __init__(self):
        self.color = None
        self._content = None
        
    def fill(self,beverage):
        self._content = beverage
        
    def empty(self):
        self._content = None


# In[39]:

cup = Cup()


# In[41]:

cup._content = 'tea'


# In[42]:

cup._content


# In[43]:

# Private


# In[49]:

class Cup:
    def __init__(self,color):
        self._color = color # protected
        self.__content = None # private
        
    def fill(self,beverage):
        self.__content = beverage
        
    def empty(self):
        self.__content = None


# In[50]:

redCup = Cup('red')


# In[51]:

redCup._color


# In[52]:

redCup._Cup__content = 'tea'


# In[53]:

redCup._Cup__content


# In[55]:

# object._<name_of_the_class>__<name_of_the_private_attribute>


# In[58]:

# Exception Handling 


# In[59]:

a = [1,2,3]


# In[60]:

a


# In[61]:

print ("second element", a[1])
#print ('Forth element', a[3])


# In[62]:

try:
    print ("second element", a[1])
    print ('Forth element', a[3])
except IndexError:
    print ('An Index Error Occured')


# In[63]:

# IndexError, ImportError, IOError, ZeroDivisionError, TypeError


# In[68]:

try:
    #print ("second element", a[1])
    #print ('Forth element', a[3])
    a = 3
    b = a
    c = 4
    #print (b)
except IndexError:
    print ('An Index Error Occured')
except ZeroDivisionError:
    print ('A Zero Division error occurred')
else:
    print (c)


# In[2]:

try:
    f = open("myfile","w")
    a,b = [int(x) for x in input("Enter two numbers:").split()]
    c = a/b
    f.write("writing %d into myfile" %c)
    
except ZeroDivisionError:
    print ('Division by zero happened')
    print ('Please do not enter 0 in input')
finally:
    f.close()
    print ('Fil')


# In[ ]:
'''
try:
    statements
except Exception1:
    handler1
except Exception2:
    handler2
else:
    statements
finally:
    statements. 
'''

# In[4]:

#1. Compile-time error
#2. Runtime errors
#3. Logical errors


# In[8]:

x = 1
if x == 1:
    print ('Where is the colon')


# In[9]:

# runtime error 


# In[10]:

def add_sum(a,b):
    print (a+b)


# In[11]:

add_sum('Hi',25)


# In[12]:

# logical error 


# In[ ]:

ArithmeticError
AssertionError
EOFError
IOError
ImportError
IndexError
KeyError
NameError
OverFlowError
RuntimeError
ValueError
IndentationError


# In[13]:

# example of IOError


# In[16]:

try:
    name = input('Enter Filename: ')
    f = open(name,'r')
except IOError:
    print ('File not found: ', name)
else:
    n = len(f.readlines())
    print (name,'has',n,'lines')
    f.close()


# In[ ]:

#except Exceptionclass

#or 

#except Exceptionclass as obj:
    
#or 

#except (ExceptionClass1,Exception2,)

#or except(TypeError,ZeroDivisionError):
#    print ('Either TypeError or ZeroDivisionError Occurred')
    
#exception:
#    print ('Some exception occurred')



# In[18]:

try:
    x = int(input('Enter a number: '))
    y = 1/x
finally:
    print ("Not catching any error")
print ('The inverse is: ', y)


# In[19]:

# The assert statement


# In[ ]:

assert condition,message


# In[1]:

try:
    x = int(input('Enter a number between 5 and 10'))
    assert x>=5 and x<=10
    print ('The number entered: ', x)
except AssertionError:
    print ('The condition is not fulfilled')


# In[22]:

# user-defined exception


# In[31]:

# create our own class as sub class to Exception class
class MyException(Exception):
    def __init__(self,arg):
        self.msg = arg
        
    def check(dict):
        for k,v in dict.items():
            print ('Name={:15s} Balance = {:10.2f}'.format(k,v))
            if (v<2000.00):
                raise MyException('Balance amount is less in the account of '+ k)
                
    bank = {'Raj':5000.00,'Vani':8900.50, 'Ajay':1990.00,'Naresh':3000.00}
    try:
        check(bank)
    except MyException as me:
        print (me)


# In[32]:

bank = {'Raj':5000.00,'Vani':8900.50, 'Ajay':1990.00,'Naresh':3000.00}


# In[33]:

bank


# In[34]:

bank.items()


# In[ ]:



