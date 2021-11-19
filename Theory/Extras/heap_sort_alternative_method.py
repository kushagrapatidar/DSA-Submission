#Alternative Method
#Heap Sort

#Heap Sort Function:
def heapSort(arr):
    n=len(arr)-1
    
    for j in range(2):
        i=n
        
        while i>0:
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
        
            if arr[i-1]>arr[(i-1)//2]:
                arr[i-1],arr[(i-1)//2]=arr[(i-1)//2],arr[i-1]
            i-=2
        
        arr[0],arr[n]=arr[n],arr[0]
    return arr

#Driver Code
if True:
    arr=[3,7,1,8,2,5,9,4,6]
    print(arr,"\n")
    i=len(arr)
    while i>0:
        arr[:i]=heapSort(arr[:i])
        i-=1
    print(arr)

#Rough Work
    #Corresponding parent and first chil node
    # 2:1:0
    # 4:3:1
    # 6:5:2
    # 8:7:3
    # i-1:((i-1)/2) #General Indexing 