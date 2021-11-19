#Experiment: 12
str='apple mango apple orange orange apple guava mango mango'
str_lst=str.split()

WordCount=dict()
count=0
for key in str_lst:
    if key not in WordCount.keys():
        WordCount[key]=1
    else:
        WordCount[key]+=1
WordCount=sorted(WordCount.items(),key=lambda item: item[1],reverse=True)
for (k,v) in WordCount:
    print(k+" : ",v)
print("\r")
for (k,v) in WordCount:
    if count == 0:
        count=v
        print("Word with maximum number of occurence is '"+k+"' : Number of Occurence",v)
    elif v == count:
        print("Word with maximum number of occurence is '"+k+"' : Number of Occurence",v)