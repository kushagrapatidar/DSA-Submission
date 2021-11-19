#Counting Sort

#Counting Sort Function
def countingsort(arr):
    count=dict()
    for ele in arr:
        if ele not in count:
            count[ele]=1
        else:
            count[ele]+=1
    Count=sorted(count)
    next=0
    for ele in Count:
        i=0
        for i in range(count[ele]):
            arr[i+next]=ele
        next+=i+1
    return arr

#Driver Code
'''
if True:
    arr=[0,1,4,2,4,7,2,6,3,4,0,2,9,4,9,3,5,6,8,7,5,8]
    print(arr)
    arr=countingsort(arr)
    print(arr)'''