def get_connectivity_lst(i,lst,lst2):
    if i not in lst.keys():
        return False
    nodes=lst[i]
    for j in range(len(nodes)):
        if nodes[j][1] not in lst2:
            lst2.append(nodes[j][1])
            lst2=get_connectivity_lst(nodes[j][1],lst,lst2)
    return lst2

def check_connectivity(graph):
    lst=dict()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]==1:
                if i not in lst.keys():
                    lst[i]=[[i,j]]
                else:
                    lst[i].append([i,j])
    print(lst)
    
    for i in lst.keys():
        lst2=list()
        lst2.append(i)
        lst2=get_connectivity_lst(i,lst,lst2)
        print(lst2)
        if lst2==False or len(lst2)!=len(graph):
            return False
        
    return True

def print_graph(graph):
    n=len(graph)
    print('   ',end='')
    [print(f'\033[1;33;40m{x}',end="  ") for x in range(1,n+1)]
    print('\n')
    for i in range(1,n+1):
        print(f'\033[1;31;40m{i}\033[1;37;40m',end="  ")
            
        for j in range(1,n+1):
            print(f'{graph[i-1][j-1]}',end="  ")
        print("\n")

#Driver Code
if True:
    #Strongly Connected Graph
    graph=[[0,0,0,1,1],
           [1,0,0,0,0],
           [0,0,0,1,0],
           [0,1,1,0,0],
           [1,0,0,0,0]]
    #Strongly Connected Graph
    # graph=[[0,0,0,1],
    #        [1,0,0,0],
    #        [0,0,0,1],
    #        [0,1,1,0]]
    print_graph(graph)
    print("\033[1;37;40m")
    
    if check_connectivity(graph):
        print('The graph is strongly connected.')
    else:
        print('The graph is not strongly connected.')
    print("\033[0;37;40m")

