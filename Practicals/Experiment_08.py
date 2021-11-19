class TreeNode:
    data=None
    right=None
    left=None

def insert(key,root=None):
    if root==None:
        root=TreeNode()
        root.data=key
        return root
    else:
        if root.data==key:
            return root
        elif root.data<key:
            root.right=insert(key,root.right)
        else:
            root.left=insert(key,root.left)
    return root

def printbst_incr(root):
    if root:
        printbst_incr(root.left)
        print(root.data)
        printbst_incr(root.right)

#Driver Code
if True:
    n=int(input('Enter the number of nodes: '))
    r=None
    for i in range(n):
        if r==None:
            r=insert(int(input('Enter Node data: ')))
        else:
            insert(int(input('Enter Node data: ')),r)
    print('\n')
    printbst_incr(r)
    #Test Case
        # r=insert(50)
        # insert(30,r)
        # insert(20,r)
        # insert(40,r)
        # insert(70,r)
        # insert(60,r)
        # insert(80,r)
