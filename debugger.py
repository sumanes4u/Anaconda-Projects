import pdb
class ExampleClass(object):
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def exampledisp(self):
        pdb.set_trace()
        return "the name of the person is {} and number is {}".format(self.name,self.number)
    
#example = ExampleClass('suman',100)    
if __name__ == '__main__()':
    example = ExampleClass('suman',100)
    print(example.exampledisp())
    
        