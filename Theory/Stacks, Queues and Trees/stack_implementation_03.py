# Python program to
# demonstrate stack implementation
# using queue module
 
 
from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize = 3)
 
# qsize()
print(stack.qsize())
  
# put()
stack.put('a')
stack.put('b')
stack.put('c')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get()
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())