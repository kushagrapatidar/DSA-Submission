#Heapyfy Function
def heapyfy(tree_root):
    right=tree_root.right
    left=tree_root.left
    
    if right!=None:
        right=heapyfy(right)
    if left!=None:
        left=heapyfy(left)
    
    if right==None and left==None:
        return tree_root
    
    elif left==None:
        if right.data>tree_root.data:
            tree_root.right,tree_root.left=right.right,right.left
            right.right,right.left=tree_root,left
            tree_root=right

    elif right==None:
        if left.data>tree_root.data:
            tree_root.right,tree_root.left=left.right,left.left
            left.left,left.right=tree_root,right
            tree_root=left

    elif max(tree_root.data,max(right.data,left.data))!=tree_root.data:
        if max(right.data,left.data)==right.data:
            tree_root.right,tree_root.left=right.right,right.left
            right.right,right.left=tree_root,left
            tree_root=right
        else:
            tree_root.right,tree_root.left=left.right,left.left
            left.left,left.right=tree_root,right
            tree_root=left

    return tree_root
