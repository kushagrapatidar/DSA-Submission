#Quick Sort

#Partition Function
def partition(start,end,arr):
    #Assigning the pivot element, start index and end index
    piv=arr[start]
    i=start
    j=end

    while i<j: #If i>j the traversal is complete
        
        while arr[i]<=piv and i<end: i+=1 #If current(from the start) element is greater then pivot element we hold the index
        
        while arr[j]>piv and j>start: j-=1 #If current(from the end) element is smaller then pivot element we hold the index
        
        if i<j: #If the traversal is not complete
            arr[i],arr[j]=arr[j],arr[i] #Swap the current elements in hold
    
    arr[j],arr[start]=arr[start],arr[j] #Swap the last swaped element smaller than pivot with pivot after the traversal is complete
    
    return j

#Quick Sort Function
def quicksort(start,end,arr):
    if start<end: #Function will execute only if there are atleast 2 elements in arr
        
        piv_index=partition(start,end,arr) #Pivot element index obtained from Partition Function

        #Sorting the partitions on both the sides of pivot element
        quicksort(start,piv_index-1,arr) #Sorting the left half
        quicksort(piv_index+1,end,arr)   #Sorting the right half
        
    return arr
#Driver Code
'''
if True:
    arr=[7,6,10,5,9,2,213,1,15,10,25,7]
    print("Given array is\n",arr)
    arr=quicksort(0,len(arr)-1,arr).copy()
    print("Sorted array is:\n",arr)'''