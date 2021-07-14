# BFS Breadth first search
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')
            
 #--------------------------------------           
def bfs(s):
    global level
    level[s] = 0
# уровень начальной вершины
    queue = [s]
 # добавляем начальную вершину в очередь
    while queue:
 # пока там что-то есть
        v = queue.pop(0)
 # извлекаем вершину
        for w in adj[v]: 
# запускаем обход из вершины v
            if level[w] == -1: 
# проверка на посещенность
                queue.append(w) 
# добавление вершины в очередь
                level[w] = level[v] + 1 
# подсчитываем уровень вершины

for i in range(len(adj)):
    if level[i] == -1:
        bfs(i)
 # на случай, если имеется несколько компонент связности

print(level[2]) 
# уровень вершины 2