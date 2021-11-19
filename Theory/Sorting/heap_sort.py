#Heap Sort

#Heap Sort Function:
def heapsort(arr):
    n=len(arr)-1

    #Loop to create a Max Heap
    #Running the Loop the loop twice ensures that all the nodes are at the correct indices and all the greater child node comes first in the children node pair
    for j in range(2):
        i=n

        #Loop to arrange the parent nodes at its has to be index and also arranging a greater child element befor the smaller one in a children node pair
        while i>0:
            
            #Arranging a greater child element befor the smaller one in a children node pair
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
            
            #Arrangin a Parent Node to its rightful index in a particular Branch of the heap
            if arr[i-1]>arr[(i-1)//2]:
                arr[i-1],arr[(i-1)//2]=arr[(i-1)//2],arr[i-1]
            i-=2
        #print(arr)
    
    #Exchanging the last and first element in arr, i.e., setting the Largest element at the last index
    arr[0],arr[n]=arr[n],arr[0]
    
    return arr

def call_sort(arr):
    i=len(arr)

    #Loop to call heapSort on a particular segment of arr by decreasing the length from the end
    while i>0:
        arr[:i]=heapsort(arr[:i])
        i-=1

#Driver Code
'''
if True:
    arr=[3,7,1,8,2,5,9,4,6]
    print('Initial Array:\n',arr,"\n")
    call_sort(arr)

    print('Sorted Array:\n',arr)'''

#Rough Work

    #Corresponding parent and first chil node
    # 2:1:0
    # 4:3:1
    # 6:5:2
    # 8:7:3
    # i-1:((i-1)/2) #General Indexing 