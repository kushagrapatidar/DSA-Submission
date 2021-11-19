#Functions to check if the tree is full or not
def check_full(tree_root):
    if tree_root==None:
        return False
    
    if tree_root.left==None and tree_root.right==None:
        return True
    
    if tree_root.left!=None and tree_root.right!=None:
        return (check_full(tree_root.left) and check_full(tree_root.right))
    
    return False

def isfull(tree_root):
    val=check_full(tree_root)
    if val:
        print("Tree if Full")
        return True
    else:
        print("Tree is not Full")
        return False

#Function to check if a tree is perfect or not
def isperfect(tree_root):
    if check_full(tree_root):    
        from binary_tree_height import find_height_ll
        max_height,min_height=find_height_ll(tree_root)
        
        val=(max_height==min_height)
        if val:
            print("Perfect Tree")
            return True
        else:
            print("Not Perfect Tree")
            return False 
    else:
        print("The Tree is not Perfect!!")