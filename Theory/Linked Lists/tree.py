class TreeNode:
    data=None
    pos=None
    next=None
    right=None
    left=None
class Node:
    data=None
    pos=None
    next=None

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

def sort_tree_lst(tree):
    for i in range(len(tree)):
        if i!=tree[i].pos:
            tree[i],tree[tree[i].pos]=tree[tree[i].pos],tree[i]

def get_tree(tree_root,tree):
    while tree_root!=None:
        tree.append(tree_root)
        tree_root=tree_root.next
    return tree

def print_tree(tree_root):
    tree=[]
    tree=get_tree(tree_root,tree)
    i=0
    tree=sort_tree_lst(tree)
    while i<len(tree):
        if pow(2,i)<len(tree):
            for j in range(i,pow(2,i)+1):
                print(f"{tree[j].data}",end=" ")
            print("\r")
        i+=pow(2,i)

#Insert Operations    
def insert_end(head,tail,data):
    newNode=Node()
    newNode.data=data
    if tail==None:
        head=tail=newNode
    else:
        tail.next=newNode
        tail=newNode
    
    return head,tail

def create_tree(tree_root):
    tree_lst=[]
    while tree_root!=None:
        tree_lst.append(tree_root)
        tree_root=tree_root.next
    tree=[]
    for i in range(len(tree_lst)):
        tree_node=TreeNode()
        tree_node.data=tree_lst[i].data
        tree_node.pos=tree_lst[i].pos
        tree_node.next=tree_lst[i].next
        tree.append(tree_node)
    #[print(_.data,end=" ") for _ in tree_lst]
    for i in range(len(tree)//2):
        try:
            tree[i].left,tree[i].right=tree[2*i+1],tree[2*i+2]
        except IndexError:
            tree[i].left=tree[2*i+1]
    tree_root=tree[0]
    return tree_root

def make_tree():
    ch=int(input("Enter the number of elements: "))
    head=tail=None
    while ch>0:
        data=input('Enter the data: ')
        head,tail=insert_end(head,tail,data)
        ch-=1
    set_pos(head)
    # temp=head
    # while temp!=None:
    #     print(temp.data,":",temp.pos)
    #     temp=temp.next
    tree_root=create_tree(head)
    return  tree_root
