#Experiment: 15
def make_words(arr):
    words=list()
    word=""
    
    #For first word
    for _ in arr:
        if 0<_<27:
            word+=chr(_+64)
        else:
            word+=str(_)
    words.append(word)

    for i in range(len(arr)):
        word=""
        combination=[]
        combination1=[]

        #For creating word from numbers before i in arr 
        for _ in range(i):
            if 0<arr[_]<27:
                combination.append(chr(arr[_]+64))
            else:
                combination.append(str(arr[_]))
            

        while i<len(arr):
            j=i+1
            if i==len(arr)-1: #If the last element in arr 
                if 0<arr[i]<27:
                    combination.append(chr(arr[i]+64))
                else:
                    combination.append(str(arr[i]))
                i+=1
                  

            elif 0<arr[i]*10+arr[j]<27 and 0<arr[j]<10: #If Valid Pair
                temp=combination.copy()
                combination.append(chr(arr[i]*10+arr[j]+64))
                if j>3: 
                    combination1=temp.copy()                           #Making another parallel combination
                    combination1.append(chr(arr[i]+64)+chr(arr[j]+64))  
                i+=2
                
            
            elif 0<arr[j]<10: #If the pair is Invalid
                if 0<arr[i]<27:
                   combination.append(chr(arr[i]+64))
                else:
                    combination.append(str(arr[i]))
                i+=1 
            
            else:
                if 0<arr[i]<27:   #If curr element is valid number
                    combination.append(chr(arr[i]+64))
                else:
                    combination.append(str(arr[i]))

                if 0<arr[j]<27: #If next element is valid number
                    combination.append(chr(arr[j]+64))
                else:
                    combination.append(str(arr[j]))
                i+=2

        #Creating the words
        #print(combination)
        for _ in combination:
            word+=_
        words.append(word)
        
        word=""
        #print(combination1)
        for _ in combination1:
            word+=_
        words.append(word)
    
    words.sort() #Arranging the same words together
    #print(words)
    
    #Creating a cleaned word list
    wordlst=list()
    for i in range(len(words)):
        if i==len(words)-1:
            wordlst.append(words[i])
        elif words[i]!=words[i+1]:
            wordlst.append(words[i])
    return wordlst

def print_words(words):
    words=words[1:]
    for word in words:
        print(word)

#Driver Code
if True:
    #Test Cases
    arr=[1,2,2]
    #arr=[1,2,2,1]
    #arr=[1,15,2,1]
    #arr=[1,29,2,1]
    #arr=[1,2,2,27,1,2]
    #arr=[1,29,2,2,27,1,2]

    words=make_words(arr)
    print_words(words)