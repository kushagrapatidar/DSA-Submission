#Driver Code: Binary Tree Height
if True:
    from binary_tree_height import find_height

    arr=[2,3,9,4,5] #height = 2 , (2->3->4,5)
    height=find_height(arr,0)
    print(f'Height of the tree {arr} is {height}')

    arr=[2,3,9,4,5,10,11,6] #height = 3, (2->3->4->6)
    height=find_height(arr,0)
    print(f'\nHeight of the tree {arr} is {height}')#'''