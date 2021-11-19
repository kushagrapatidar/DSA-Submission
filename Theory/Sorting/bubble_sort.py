#Bubble Sort

#Bubble Sort Function
def sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            num=arr[i]
            next_num=arr[i+1]
            if num>next_num:
                arr[i]=next_num
                arr[i+1]=num

#Driver Code
'''
if True:
    arr=[7,6,10,5,9,2,213,1,15,10,25,7]
    print(arr)
    bubbleSort(arr)
    print(arr)'''