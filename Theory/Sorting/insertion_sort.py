#Insertion Sort

#Insertion Sort Function
def insertionSort(arr):
    l=len(arr)
    print(arr)
    for i in range(1,l):
        store=arr[i]
        j=i-1
        while j>=0 and store<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=store

#Driver Code
'''
if True:
    arr=[7,6,10,5,9,2,213,1,15,10,25,7]
    insertionSort(arr)
    print(arr)'''