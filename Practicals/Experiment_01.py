#Experiment: 01
arr=[1,4,85,23,5,2,3,9,6,0,1]
lst=list()
sum=6
for ele in arr:
    for _ in arr:
        if ele+_==sum and [ele,_] not in lst and [_,ele] not in lst:
                lst.append([ele,_])
                print((ele,_))