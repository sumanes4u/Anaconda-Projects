str = 'Today is my lucky day'

print (str)          # Prints complete string
print (str[0] )      # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])
print (str[:7]  )    # Prints string starting from 3rd character
print (str * 2 )     # Prints string two times
print (str + "TEST") # Prints concatenated string
print (str[0:5:2])

print ('====== 2 ========')



print (str[::-1])

#print str[-1]


#print str[5:2:-1];print str[::-1];
str[-3]
print (str[-1:-5:-1])

str="HelloPython"
# 1 2 3 4 5 6 7 8 9 10 11
# H e l l 0 P y t h o n

# String Slices


print (str[1:5:2]) #begin,end,step
print (str[5:])
print (str[-5])  #from last
print (str[15:])  #no output ; no exception is thrown like in C, C++ etc.
print (str[:])

#reverse string
print (str[-1::-1])
print (str[::-1])

print (str[-2:-5:-1])


#Tuple
str2=(1,2,3,"hello",True,None,7,8,9,0,5,4) #heterogenious array
print (str2[::-1])

data=(1,2,3,4,5)
data = (100,200)  #overwrites
print (data)

s = 'United States of America'

print ( s.lower(), s.upper() ) # -- returns the lowercase or uppercase version of the string
print ( s.strip() ) # -- returns a string with whitespace removed from the start and end
print ( s.isalpha() )
print ( s.isdigit() )
print ( s.isspace() ) # ... -- tests if all the string chars are in the various character classes
print ( s.startswith('other') )
print ( s.endswith('other') ) # -- tests if the string starts or ends with the given other string
print ( s.find('other') ) # -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
print ( s.replace('old', 'new') ) # -- returns a string where all occurrences of 'old' have been replaced by 'new'
print ( s.split('delim') ) # -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
print ( s.join(list) ) # -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc


