import stack

mystack = stack.getStack()

for item in range(1,5):
    stack.push(mystack, item)
    print('Pushing', item, 'on stack')

while not stack.isEmpty(mystack):
    item = stack.pop(mystack)
    print('Popping', item,'from stack')



