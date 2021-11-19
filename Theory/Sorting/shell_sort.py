#Shell Sort

#Using Shell Sequence
#gap=gap//2
def construct_shell_gap_sequence(max_size):
    seq_lst=list()
    gap=max_size//2
    while gap>0:
        seq_lst.append(gap)
        gap=gap//2
    
    return seq_lst

#Using Knuth Sequence
#gap=3^k-1//2
def construct_knuth_gap_sequence(max_size):
    seq_lst=list()
    gap_index=1
    while (pow(3,gap_index)-1)//2<max_size:
        seq_lst.append((pow(3,gap_index)-1)//2)
        gap_index+=1
    
    n=len(seq_lst)
    for i in range(n//2):
        seq_lst[i],seq_lst[n-i-1]=seq_lst[n-i-1],seq_lst[i]
    return seq_lst

#Using Pratt Sequence
#gap=2^p X 3^q
def construct_pratt_gap_sequence(max_size):
    seq=dict()
    lst=list()
    
    _=0
    while pow(2,_)<max_size:
        lst.append(pow(2,_))
        _+=1
    
    _=0
    while pow(3,_)<max_size:
        key=pow(3,_)
        temp=list()
        for ele in lst:
            if key*ele<max_size:
                temp.append(key*ele)
        seq[key]=temp
        _+=1

    seq_lst=list()
    for key in seq.keys():
        for _ in seq[key]:
            seq_lst.append(_)
    
    seq_lst.sort()
    n=len(seq_lst)
    for i in range(n//2):
        seq_lst[i],seq_lst[n-i-1]=seq_lst[n-i-1],seq_lst[i]
    return seq_lst

#Customized Sort Function to work over Shell, Knuth & Pratt Gaps
def shellsort(arr):
    n=len(arr)
    seq=input("Enter the sequence:('Shell' or 'Knuth' or 'Pratt'): ")
    while True:
        if seq=='Shell' or seq=='shell':
            gap_sequence=construct_shell_gap_sequence(n)
            break
        elif seq=='Knuth' or seq=='knuth':
            gap_sequence=construct_knuth_gap_sequence(n)
            break
        elif seq=='Pratt' or seq=='pratt':
            gap_sequence=construct_pratt_gap_sequence(n)
            break
        else:
            print('Choose again!!')
    print(f'Gap sequence used: {gap_sequence}\n')
    p=1
    
    for gap in gap_sequence:
        #print("Pass:",p,"\n")
        #print("Gap:",gap,"\n")
        p+=1
    
        for i in range(n-gap):
            j=i+gap
    
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            k=i
    
            while k>0:
                if arr[k]<arr[k-gap]:
                    arr[k],arr[k-gap]=arr[k-gap],arr[k]
                k-=gap
    
            #print(i,":",arr)
        #print("\n")
    return arr

#Driver Code
'''
if True:
    arr=[3,7,1,8,2,5,9,4,6]
    #arr=[23,29,15,19,31,7,9,5,2]
    print(f"Initial Array:\n{arr}\n")

    arr=shellsort(arr)
    print(f"Sorted Array:\n{arr}")'''