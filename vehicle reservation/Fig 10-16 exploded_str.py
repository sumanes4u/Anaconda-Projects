# Exploded String Class

class ExplodedStr(str):

    def __init__(self, value = ''):
        
        # call to init of str class
        str.__init__(value)


    def explode(self):
        
        # empty str returned unaltered
        if len(self) == 0:
            return self
        else:
            # create exploded string
            empty_str = ''
            blank_char = ' '
            temp_str = empty_str
            
            for k in range(0, len(self) - 1):
                temp_str = temp_str + self[k] + blank_char
                
            # append last char without following blank
            temp_str = temp_str + self[len(self)- 1]
                
            # return exploded str by joining all chars in list
            return temp_str
