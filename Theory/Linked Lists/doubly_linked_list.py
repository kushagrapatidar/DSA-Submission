class Node:
    prev=None
    data=None
    next=None
    pos=None

def set_pos(head):
    head.pos=1
    temp=head
    currPos=1
    while temp!=None:
        currPos=temp.pos
        temp=temp.next
        try:
            temp.pos=currPos+1
        except AttributeError:
            continue

#Insert Operations    
def insert_beg(head,data):
    newNode=Node()
    newNode.data=data
    newNode.next,head.prev=head,newNode
    head=newNode
    return head

def insert_bet(head,tail,pos,data):
    if pos==1:
        head=insert_beg(head,data)
    elif pos>tail.pos:
        tail=insert_end(tail,data)
    else:            
        currNode=head
        while currNode.pos<pos-1:
            currNode=currNode.next
        nextNode=currNode.next

        if nextNode!=None:
            newNode=Node()
            newNode.data=data
            newNode.prev,currNode.next=currNode,newNode
            newNode.next,nextNode.prev=nextNode,newNode

    return head,tail

def insert_end(tail,data):
    newNode=Node()
    newNode.data=data
    newNode.prev,tail.next=tail,newNode
    tail=newNode
    return tail

########################################################################################################################################################################
#Delete Operations
def delete_beg(head):
    print(f"Data at the deleted Node: {head.data}")
    temp=head
    head=None
    head=temp.next
    head.prev=None
    set_pos(head)
    return head

def delete_bet(head,tail,pos):
    if pos==1:
        head=delete_beg(head)
    else:
        temp=head
        while temp!=None:
            if temp.pos==pos:
                print(f"Data at the deleted Node: {temp.data}")
                break
            temp=temp.next
        try:
            temp.prev.next,temp.next.prev=temp.next,temp.prev
            temp=None
        except AttributeError:
            tail=delete_end(tail)
    set_pos(head)
    return head,tail

def delete_end(tail):
    print(f"Data at the deleted Node: {tail.data}")
    temp=tail
    tail=None
    tail=temp.prev
    tail.next=None
    return tail

########################################################################################################################################################################
#Miscellaneous Operations
#Reverse Operation
def reverse(head,tail):
    temp=head
    while temp!=None:
        temp.prev,temp.next=temp.next,temp.prev
        temp=temp.prev
    head,tail=tail,head
    set_pos(head)
    return head,tail

#Traverse Operation
def traverse(head):
    temp=head
    data=""
    posStr=""
    while temp!=None:
        data+=str(temp.data)+" "
        posStr+=str(temp.pos)+" "
        temp=temp.next
    
    print(data+"\n"+posStr)
    return data,posStr

#Sort Operation #Under Developement
def sort_data(head):
    data,posStr=traverse(head)
    Bool=False
    data=data.split()
    for _ in data:
        if isinstance(_,str):
            Bool=True

    if Bool:
        data.sort()
    
    else:
        for _ in data:
            if isinstance(_,float):
                Bool=True
        if Bool:
            data=float(data)
        else:
            data=int(data)
        data.sort()
    return data

def sort(head,tail): #CONTINUE HERE
    data=sort_data(head)
    temp1=temp2=head
    index=0
    while temp1!=None:
        while temp2!=None:
            if temp2.data in data:
                index=data.index(temp2)
    return head,tail

#Search Operation
def search(head,data=None):
    pos=[]
    if data==None:
        data=input('Enter the data to be searched: ')
    try:
        try:
            data=int(data)
        except ValueError:
            data=float(data)
    except ValueError:
        data=str(data)
    temp=head
    while temp!=None:
        if temp.data==data:
            pos.append(temp.pos)
        temp=temp.next
    if len(pos)!=0:
        print(f"'{data}' found at the positions {pos} in the list.")
    else:
        print(f"{data} is not in the list!!")
    return pos

#Update Operation
def update(head):
    olddata=input('Enter the data to be Updated: ')
    newdata=input('Enter the Updated data: ')
    try:
        try:
            olddata=int(olddata)
        except ValueError:
            olddata=float(olddata)
    except ValueError:
        olddata=str(olddata)
    try:
        try:
            newdata=int(newdata)
        except ValueError:
            newdata=float(newdata)
    except ValueError:
        newdata=str(newdata)
    pos=search(head,olddata)
    if len(pos)==0:
        print(f"The list does not contain any data,{olddata}")
    
    else:
        temp=head
        while temp!=None:
            if temp.pos in pos:
                temp.data=newdata
            temp=temp.next
    print("List updated successfully!!")

#Swap with head Operation #Under Developement
def swap_with_head(head):
    pos=int(input('Enter the position of the node to be swapped with head node: '))
    temp=head
    while temp!=None:
        if temp.pos==pos:
            break
        temp=temp.next
    if temp==None:
        print(f"Position {pos} does not exist!!")
        return head
    
    prev=temp.prev
    head.prev,temp.prev=temp.prev,head.prev
    head.next,temp.next=temp.next,head.next
    head.pos,temp.pos=temp.pos,head.pos
    prev.next=head
    head=temp
    return head

########################################################################################################################################################################
#Insert Function
def insert(head,tail):
    data=input('\nEnter the data: ')
    
    if head==None or tail==None:
        print("\nThe List is Empty!!\nCreating the first Node...\n")
        head=Node()
        head.data=data
        head.pos=1
        tail=head
        print("Node created successfully!!")

    else:
        ch=input("Enter the position of insertion:'B' for Beginnig, 'E' for End or Position in numbers greater than or equal to 1: ")
    
        try:
            ch=int(ch)
            head,tail=insert_bet(head,tail,ch,data)
        except ValueError:
            if ch=='B' or ch=='b':
                head=insert_beg(head,data)
            elif ch=='E' or ch=='e':
                tail=insert_end(tail,data)
    
        set_pos(head)
    return head,tail

#Delete Function
def delete(head,tail):
    ch=input("Enter the position of deletion:'B' for Beginnig, 'E' for End or Position in numbers greater than or equal to 1: ")
    try:
        ch=int(ch)
        head,tail=delete_bet(head,tail,ch)
    except ValueError:
        if ch=='B' or ch=='b':
            head=delete_beg(head)
        elif ch=='E' or ch=='e':
            tail=delete_end(tail)
    
    set_pos(head)
    return head,tail

########################################################################################################################################################################
#Functions to call insert and delete functions
def call_insert(head,tail):
    num=int(input('Enter the number of elements to be inserted: '))
    for _ in range(num):
        head,tail=insert(head,tail)

    return head,tail

def call_delete(head,tail):
    num=int(input('Enter the number of elements to be deleted: '))
    for _ in range(num):
        head,tail=delete(head,tail)

    return head,tail

########################################################################################################################################################################
#Operate Function to choose the operation
def operate(head,tail):        
    ch=input("Enter the operation:\n'I' to Insert\n'D' to Delete\n'Sr' to Search\n'U' to Update\n'R' to Reverse\n'St' to Sort\n'T' to Traverse\n'Sw' to Swap a node with head node\nYour Choice: ")
    empty_list="The List is Empty!!"
    if ch=='I' or ch=='i':
        head,tail=call_insert(head,tail)
        
    elif ch=='D' or ch=='d':
        if head==None or tail==None:
            print(empty_list)
        else:
            head,tail=call_delete(head,tail)
        
    elif ch=='R' or ch=='r':
        if head==None or tail==None:
            print(empty_list)
        else:
            head,tail=reverse(head,tail)
        
    elif ch=='T' or ch=='t':
        if head==None or tail==None:
            print(empty_list)
        else:
            traverse(head)
        
    elif ch=='U' or ch=='u':
        if head==None or tail==None:
            print(empty_list)
        else:
            update(head)
        
    elif ch.upper()=='SR':
        if head==None or tail==None:
            print(empty_list)
        else:
            search(head)
        
    elif ch.upper()=='ST':
        if head==None or tail==None:
            print(empty_list)
        else:
            print("Sort Under Developement!!")
            #head,tail=sort(head,tail)

    elif ch.upper()=='SW':
        if head==None or tail==None:
            print(empty_list)
        else:
            print("Swap Under Developement!!")
            #swap_with_head(head)

    else:
        print("Invalid Choice!!\nPlease try again...\n")
        operate(head,tail)
    
    ch=input("Do you want to conduct more operations??('Y' for yes & 'N' for no): ")
    if ch=='Y' or ch=='y':
        operate(head,tail)
