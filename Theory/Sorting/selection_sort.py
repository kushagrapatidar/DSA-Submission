#Selection Sort

#Selection Sort Function
def sort(arr):
    for j in range(len(arr)-1):
        for i in range(j+1,len(arr)):
            if arr[i]<arr[j]:
                arr[j],arr[i]=arr[i],arr[j]

#Driver Code
'''
if True:    
    arr=[7,6,10,5,9,2,213,1,15,10,25,7]
    print(arr)
    selectionSort(arr)
    print(arr)'''