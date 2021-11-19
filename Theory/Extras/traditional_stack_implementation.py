#Stack Implementation using traditional methods
#Class Stack
class Stack:
    obj=None
    address=None

#Push Function
def push(ele, add):
    stk=Stack()
    stk.obj=ele
    stk.address=add
    return stk

def pop(ele,add):
    stk=Stack()


empty=""
i_add=add=id(empty)
print(add)
ch=''
size=0
x=Stack()
n=int(input('Enter the number of elements:'))
for _ in range(n):
    ch=input("Enter your choice, Push, Pop or Size: ")
    if ch == "push" or ch == "Push":
        ele=input("Enter:")
        x=push(ele,id(x))
        add=id(x)
        size+=1
    elif ch == "pop" or ch == "Pop":
        if size==0:
            print("Stack Underflow!!")
        else:
            x=Stack()
            x=pop(x,add)
            size-=1
    

    if _ == n-1:
        ch=input("Do you want to continue?('Y' for yes and 'N' for no)")
        if ch == 'y' or ch == 'Y':
            n=int(input('Enter the number of elements:'))
            _=0