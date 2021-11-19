#Experiment: 05
num=list()
num.append(input('Enter a number: '))
even_and_odd=['EVEN','ODD']
for ele in num:
    index=int(ele)%2
    print('The number '+ele+' is '+even_and_odd[index])
