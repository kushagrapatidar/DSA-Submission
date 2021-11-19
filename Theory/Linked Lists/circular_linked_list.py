class Node:
    data=None
    next=None
    pos=None

def set_pos(head):
    head.pos=1
    temp=head.next
    currPos=2
    head.pos=currPos-1
    temp.pos=currPos
    while temp!=head:
        currPos=temp.pos
        temp=temp.next
        try:
            if temp!=head:
                temp.pos=currPos+1
        except AttributeError:
            continue

#Insert Operations  
def insert_beg(head,tail,data):
    newNode=Node()
    newNode.data=data
    newNode.next=head
    tail.next=newNode
    head=newNode
    return head

def insert_bet(head,tail,pos,data):
    if pos==1 or pos>tail.pos:
        head=insert_end(head,tail,data)
    else:            
        currNode=head
        while currNode.pos<pos-1:
            currNode=currNode.next
        nextNode=currNode.next

        if nextNode!=None:
            newNode=Node()
            newNode.data=data
            currNode.next,newNode.next=newNode,nextNode

    return head,tail

def insert_end(head,tail,data):
    newNode=Node()
    newNode.data=data
    newNode.next=head
    tail.next=newNode
    tail=newNode
    return tail

########################################################################################################################################################################
#Delete Operations
def delete_beg(head,tail):
    print(f"Data at the deleted Node: {head.data}")
    tail.next=head.next
    head=head.next
    return head

def delete_bet(head,tail,pos):
    if pos==1:
        print(f"Data at the deleted Node: {head.data}")
        head=head.next
        tail.next=head
    else:
        temp=head
        prevNode=None
        while temp!=None:
            if temp.pos==pos:
                print(f"Data at the deleted Node: {temp.data}")
                break
            prevNode=temp
            temp=temp.next
        try:
            prevNode.next=temp.next
            temp=None
        except AttributeError:
            tail=delete_end(head,tail)
        set_pos(head)
    return head,tail

def delete_end(head,tail):
    print(f"Data at the deleted Node: {tail.data}")
    temp=head
    while temp.next!=tail:
        temp=temp.next
    temp.next=head
    tail=None
    tail=temp
    return tail

########################################################################################################################################################################
#Miscellaneous Operations
#Reverse Operation
def reverse(head,tail):
    node_lst=list()
    temp=head.next
    node_lst.append(head)
    while temp!=head:
        node_lst.append(temp)
        temp=temp.next
    node_lst.reverse()
    for _ in range(len(node_lst)-1):
        currNode,nextNode=node_lst[_],node_lst[_+1]
        currNode.next=nextNode
    head,tail=node_lst[0],node_lst[-1]
    tail.next=head
    set_pos(head)
    return head,tail

#Traverse Operation
def traverse(head):
    temp=head
    data=""
    posStr=""
    
    data+=str(temp.data)+" "
    posStr+=str(temp.pos)+" "
    temp=temp.next
    
    while temp!=head:
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
    temp=head.next
    if head.data==data:
        pos.append(head.pos)
    while temp!=head:
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
        temp=head.next
        if head.pos==pos:
            head.data=newdata
        while temp!=head:
            if temp.pos in pos:
                temp.data=newdata
            temp=temp.next
    print("List updated successfully!!")
    
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
        ch=input("Enter the position of insertion: 'B' for Beggining or 'E' for End or Position in numbers greater than or equal to 1: ")
    
        try:
            ch=int(ch)
            head,tail=insert_bet(head,tail,ch,data)
        except ValueError:
            if ch=='B' or ch=='b':
                head=insert_beg(head,tail,data)
            if ch=='E' or ch=='e':
                tail=insert_end(head,tail,data)
    
        set_pos(head)
    return head,tail

#Delete Function
def delete(head,tail):
    ch=input("Enter the position of deletion: 'B' for Beggining or 'E' for End or Position in numbers greater than or equal to 1: ")
    try:
        ch=int(ch)
        head,tail=delete_bet(head,tail,ch)
    except ValueError:
        if ch=='B' or ch=='b':
            head=delete_beg(head,tail)
        if ch=='E' or ch=='e':
            tail=delete_end(head,tail)
    
    if head!=None and tail!=None:
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
    if head==None or tail==None:
        print('List is empty!!')
    else:
        num=int(input('Enter the number of elements to be deleted: '))
        for _ in range(num):
            head,tail=delete(head,tail)

    return head,tail

########################################################################################################################################################################
#Operate Function to choose the operation
def operate(head,tail):        
    ch=input("Enter the operation:\n'I' to Insert\n'D' to Delete\n'Sr' to Search\n'U' to Update\n'R' to Reverse\n'St' to Sort\n'T' to Traverse\nYour Choice: ")
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
        
    else:
        print("Invalid Choice!!\nPlease try again...\n")
        operate(head,tail)
    ch=input("Do you want to conduct more operations??('Y' for yes & 'N' for no): ")
    if ch=='Y' or ch=='y':
        operate(head,tail)
