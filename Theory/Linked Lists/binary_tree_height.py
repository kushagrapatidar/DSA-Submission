#Height of a Binary Tree(Linked List)
def find_height_ll(tree_root):
    left=right=tree_root
    max_height=min_height=-1       
    while left!=None or right!=None:
        if left!=None:
            max_height+=1
            left=left.left
        if right!=None:
            min_height+=1
            right=right.right

    if max_height==-1:
        return -1,-1
    else:
        return max_height,min_height

#Height of a Binary Tree(List)
def find_height_lst(tree):
    max_height=min_height=-1
    if len(tree)==1:
        min_height=max_height=0
    elif len(tree)!=0:
        for i in range(len(tree)//2):
            if 2*i+1<len(tree):
                max_height+=1
                i=2*i+1
        for j in range(len(tree)//2):
            if 2*j+2<len(tree):
                min_height+=1
                j=2*j+2
    
    return max_height,min_height
