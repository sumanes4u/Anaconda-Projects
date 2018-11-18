class Student:
    days = 100
    def __init__(self,name,age,marks):        
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print ('Hi,My name is:%s'%self.name)
        print ('My Age is:%d'%self.age)
        print('My marks is:%d'%self.marks)        
class lab(Student):
    def __init__(self,name,age,marks,presence):
        Student.__init__(self,name,age,marks)
        self.presence = presence
    def display1(self):
        print('My Lab Status is %s'%self.presence)
        print ('Lab Marks are:%d'%self.marks)   
print(Student.days)
suman = Student('suman',32,100)
print (suman.days)
vivek = Student('vivek',32,102)
print(vivek.days)
Student.days = 145
print(Student.days)



