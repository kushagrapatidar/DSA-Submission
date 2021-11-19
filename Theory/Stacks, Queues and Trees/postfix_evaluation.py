#Evaluation Postfix Expression using Stacks
def eval(op,stack):
    a=stack.pop()
    b=stack.pop()
    if op == "+":
        result=b+a
    elif op == "-":
        result=b-a
    elif op == "*":
        result=b*a
    elif op == "/":
        result=b//a
    elif op == "%":
        result=b%a
    elif op == "^":
        result=b**a
    stack.append(result)
    return stack

#Driver Code
if True:
    #Valid Expression Test Case
    expr="231*+9-"
    #expr="12+34*-"
    
    #Invalid Expression Test Cases
    #expr="-231*+9-" 
    #expr="2231*+9-"
    #expr="21+49/*-"
    #expr="12+34*-2"
    stack = []
    x=0
    for _ in expr:
        try:
            stack.append(int(_))
        except:    
            if len(stack)>1:
                stack=eval(_,stack)
            else:
                print("Invalid Postfix Expression!!")
                x=-1
                break

    if len(stack)>1:
        print("Invalid Postfix Expression!!")
    elif x==0: print('Evaluated expression:\n"'+expr+'" =',stack.pop())