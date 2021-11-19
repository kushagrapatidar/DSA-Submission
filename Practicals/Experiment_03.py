#Experiment: 03
str=['10','68','75','7','21','12']
for j in range(len(str)):
    for i in range(len(str)-1):
        num=str[i]
        next_num=str[i+1]
        if int(num+next_num)<=int(next_num+num):
            str[i]=next_num
            str[i+1]=num
print(str)
val=''
for num in str:
    val+=num
print(int(val))