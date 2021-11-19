#Radix Sort

#Appending element in the dictionary
def app(dic=None,element=0,digit=0):
    if dic is None:
        dic=dict()
    lst=list()
    #Create a new key if digit not in dic keys and insert the element
    if digit not in dic.keys():
        lst.append(element)
        dic[digit]=lst    
    #Insert element if digit already present in dic keys
    else:
        lst=dic[digit]
        lst.append(element)
        dic[digit]=lst
    return dic
    
#Radix Sort Function
def radixsort(arr,exp,max_num):
    if max_num//exp>0: #Procedure will work only if
                       #number of recursions is less than or equal to number of digits in max_num        
        temp=dict()

        for element in arr:
            digit=(element//exp)%10 #Genrating the face value digit
            temp=app(temp,element,digit) #Append the element as per the face value digit

        array=list()
        sorted_keys=sorted(temp) #Sorted keys of temp, i,e. ordered list of current face value digits
        for i in sorted_keys: 
            lst=temp[i]
            for j in range(len(lst)):
                array.append(lst[j]) #Inserting the elements as per the order of current face value digits
        
        arr=array
        exp*=10 #Increase the value by the factor of 10
        
        #Recursive call the Radix Sort Function for sorting as per the new value of exp, i,e. as per the next greater face value digits
        arr=radixsort(arr,exp,max_num)
    return arr

#Driver Code
'''
if True:
    arr=[7,6,10,5,9,2,213,1,15,10,25,7]
    print("Initial Array:\n",arr,"\r\n")
    exp=1
    arr=radixsort(arr,exp,max(arr))
    print("Sorted Array:\n",arr)'''