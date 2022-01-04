class Node:
    def __init__(self, value):
        self.value = value

class Tree:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjency_list = [[] for i in range(vertex)]

    def add_vertex(self, src, dst):
        if src.value and dst.value < len(self.adjency_list):
            self.adjency_list[src.value-1].append(dst)
            self.adjency_list[dst.value-1].append(src)

    def find_path(self, src, dst):
        # src_node_list = self.adjency_list[src.value-1]
        visited = [False]*self.vertex    
        path=[]

        depth_first_search(src, dst, self.adjency_list, path, visited)        
        
def depth_first_search(src, dst, graph, path, visited):
    visited[src.value-1]=True
    
    #updating path list
    path.append(src.value)

    if src.value==dst.value:
        print(path)
    else:
        for vertex in graph[src.value-1]:
            if not visited[vertex.value-1]:
                depth_first_search(vertex, dst, graph, path, visited)

    path.pop()
    visited[src.value-1]=False

if __name__ == '__main__':
    t = Tree(5)

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)


    t.add_vertex(n1, n2)
    t.add_vertex(n1, n4)

    t.add_vertex(n2, n3)
    t.add_vertex(n2, n4)
    t.add_vertex(n2, n5)

    t.add_vertex(n3, n5)

    # for i in t.adjency_list[0]:
    #     print(i.value)

    t.find_path(n1, n3)


