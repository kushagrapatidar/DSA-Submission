#experiment: 02
arr=[1,4,85,23,5,2,3,9,6,0,1]
max_sum=0
lst=[]
for ele in arr:
    for _ in arr:
        if ele!=_ and ele+_>max_sum:
            max_sum=ele+_
            lst=[]
            lst.append([ele,_])
        elif ele!=_ and ele+_==max_sum and [ele,_] not in lst and [_,ele] not in lst:
            lst.append([ele,_])
print("Maximum sum:",max_sum,"\n")
print("Pairs:\n")
for [ele,_] in lst:
    print((ele,_),"\n")