#Merge Sort

#Merge Sort Function
def mergesort(arr):
    if len(arr)>1: #Condition will only work if there are atleast two elements in arr
        mid=len(arr)//2 #Mid index of arr
        
        #Division oh halves
        L=arr[:mid] #Left half of arr, i.e,before mid index
        R=arr[mid:] #Right half of arr, i.e,after mid index
        
        #Sorting both the halves
        mergesort(L)
        
        mergesort(R)
        print(R)
        
        #Arranging the elements from sorted L and R while merging in arr
        i=j=k=0
        while i<len(L) and j<len(R): #if either of the left or right is completly inserted in arr the loop will quit

            if L[i]<R[j]:   #If current element of left is smaller than current element of right
                arr[k]=L[i] #Insert the current element of left in arr
                i+=1        #Change the current index in left by +1

            else:           #If current element of left is smaller than current element of right
                arr[k]=R[j] #Insert the current element of left in arr
                j+=1        #Change the current index in left by +1
            k+=1
        
        #Inserting the remaining elements
        #If right was exhausted first
        while i<len(L): #Since i corresponds to the next to last filled element in L  
            arr[k]=L[i]
            i+=1
            k+=1

        #If left was exhausted first
        while j<len(R): #Since j corresponds to the next to last filled element in R
            arr[k]=R[j]
            j+=1
            k+=1

#Driver Code
'''
if True:
    arr=[12,11,13,2,19,21]
    print("Given array is\n",arr)
    mergesort(arr)
    print("Sorted array is:\n",arr)'''