#Check Balanced Use Of Parentheses

string="((())(()()(()()()()()()()())))(()()(()()(()()()())))"
#string="((())(()()(()()()()()()()())))(()()(()()(()()()()))"
stack=[]

for _ in string:
    if _ == '(':
        stack.append('(')
    if _ == ')' and len(stack)>0:
        stack.pop()
    elif _ == ')' and len(stack)==0:
        print("Unbalanced!!")
        break
if len(stack)==0:
    print("Balanced!!")
else:
    print("Unbalanced!!")