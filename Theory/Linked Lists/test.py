#Driver Code: Singly Linked List
'''if True:
    from singly_linked_list import operate
    head=tail=None
    operate(head,tail)
    #Test List
        #Ins - 'Lists'
        #Ins - beg - 'Linked'
        #Ins - end - 'is'
        #Ins - end - 'a'
        #Ins - 1 - 'Doubly'
        #Ins - 7 - 'Structure'
        #Ins - 6 - 'Data'
        #Trav
        #Srch - 'a'
        #Updt - 'Lists' to 'List'
        #Trav
        #Del - 5
        #Del - beg
        #Del - end
        #Trav
        #Rev
        #Trav
    #'''

#Driver Code: Doubly Linked List
'''if True:
    from doubly_linked_list import operate
    head=tail=None
    operate(head,tail)
    #Test List
        #Ins - 'Lists'
        #Ins - beg - 'Linked'
        #Ins - end - 'is'
        #Ins - end - 'a'
        #Ins - 1 - 'Doubly'
        #Ins - 7 - 'Structure'
        #Ins - 6 - 'Data'
        #Trav
        #Srch - 'a'
        #Updt - 'Lists' to 'List'
        #Trav
        #Del - 5
        #Del - beg
        #Del - end
        #Trav
        #Rev
        #Trav
    #'''

#Driver Code: Circular Linked List
'''if True:
    from circular_linked_list import operate
    head=tail=None
    operate(head,tail)
    #Test List
        #Ins - 'Lists'
        #Ins - beg - 'Linked'
        #Ins - end - 'is'
        #Ins - end - 'a'
        #Ins - 1 - 'Doubly'
        #Ins - 7 - 'Structure'
        #Ins - 6 - 'Data'
        #Trav
        #Srch - 'a'
        #Updt - 'Lists' to 'List'
        #Trav
        #Del - 5
        #Del - beg
        #Del - end
        #Trav
        #Rev
        #Trav
    #'''

#Driver Code: Tree Operations
#if True:
    # from tree import make_tree,print_tree
    # from binary_tree_height import find_height_ll
    # from heapyfy import heapyfy
    # import check_heap as CH

    # tree_root=make_tree()
    
    # #Heapyfy Operation
    # tree_root=heapyfy(tree_root)
    
    # #Heights of a Binary Tree Operation
    # max_height,min_height=find_height_ll(tree_root)

    # if max_height==-1:
    #     print("There are no Nodes")     
    # else:
    #     print(f"Maximum and Minimum heights of the tree are {max_height,min_height}")
    
    # #Full and Perfect Binary Trees
    # CH.isfull(tree_root)
    # CH.isperfect(tree_root)

    # print_tree(tree_root)
    # #Test Cases:
    #     #arr=[2,3,9,4]
    #     #max_height = 2, min_height=1
    #     #arr=[2,3,9,4,5,10,11,6]
    #     #max_height = 3, min_height = 2

#Tree printing algo Dev.
'''if True:
    from binary_tree_height import find_height_lst
    tree=[2,3,9,4,5,10,11,6,1,7,8,9,12,13,14]
    max_h,min_h=find_height_lst(tree)
    # print(max_h)
    l=0
    i=0
    k=2*pow(2,max_h-1)-1
    while l<=max_h:
        #print(' '*(k+1),end=" ")
        k=k-2
        j=0
        while j<pow(2,l) and i+j<len(tree):
            print(f"{tree[i+j]}",end=" ")
            j+=1
        print("\r")
        i=i+j

        l=l+1
    #'''