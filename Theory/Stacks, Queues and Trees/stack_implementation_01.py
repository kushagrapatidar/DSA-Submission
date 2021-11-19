# Python program to
# demonstrate stack implementation
# using list
 
 
stack = ["Python","C","Android"]
 
# append()
stack.append("Java")
stack.append("C++")
 
print('Initial stack')
print(stack)
 
# pop()
print('\nElements popped from stack:')
print(stack.pop())
print("Stack:",stack)
print(stack.pop())
print("Stack:",stack)
print(stack.pop())
print("Stack:",stack)
print(stack.pop())
print("Stack:",stack)
print(stack.pop())
print("Stack:",stack)
 
print('\nStack after elements are popped:')
print(stack)