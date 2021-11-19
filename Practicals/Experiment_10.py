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
