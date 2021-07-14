# Список смежности вершин графы  n - число вершин m - число ребер графа

# ADJACENCY LIST
def main():
    v, e = map(int, input().split()) # v вершины e ребра
    graph = {i: set() for i in range(1, v+1)} #пустой массив графа
    
    for i in range(e):
        v1, v2 = map(int, input().split())
        
        graph[v1].add(v2)
#       graph[v2].add(v1) для неориентированного графа

    for i in graph.keys():
        
        print(i,' : ', graph[i])
        
if __name__=='__main__':
    main()