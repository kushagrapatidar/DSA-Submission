#Experiment: 09
def MaxMin(arr,lb,ub,max,min):
    if lb==ub: #If there is a single element in the Partition
        
        max=min=arr[lb] #Assign the element as both 
    
    elif lb==ub-1: #If there are only two elements in the Partition
        
        #Compare and assign Maximum and Minimun to max and min
        if arr[lb]<arr[ub]:
            max=arr[ub]
            min=arr[lb]
        else:
            max=arr[lb]
            min=arr[ub]

    #If there are more than 2 elements in the Partition
    else:
        mid=(lb+ub)//2 #Assign the middle index as the mid value of Ub and Lb
        
        #min1 and max1 initializationion
        max1=0
        min1=0
        
        #Recursive call for finding Maximum and Minimum for both the partitions before and after the middle index
        max,min=MaxMin(arr,lb,mid,max,min)
        max1,min1=MaxMin(arr,mid+1,ub,max1,min1)
        
        #Compare the max and min from both the Partitions to obtain Maximum and Minimum
        if max<max1:
            max=max1
        if min>min1:
            min=min1
    
    return max,min

#Driver Code
arr=[7,6,5,9,2,1,15,10,25,7]
Max=0
Min=0
Max,Min=MaxMin(arr,0,len(arr)-1,Max,Min)
print("Maximum:",Max,"\nMinimum:",Min)