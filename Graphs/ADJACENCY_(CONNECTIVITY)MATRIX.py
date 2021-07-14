# создается матрица размером (n+1)X(n+1) 
#n - число вершин m - число ребер графа

#ADJACENCY (CONNECTIVITY) MATRIX


n, m = map(int, input().split())
A = [[0] * (n + 1) for i in range(n + 1)] #матрица развером Вершина на вершину
for i in range(m):
    u, v = map(int, input().split()) #вводим ребра
    A[u][v] = 1
    # A[v][u] = 1 - для неориентированного графа
    
    
for i in A:
    print(*i)
