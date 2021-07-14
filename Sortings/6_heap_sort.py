# To heapify subtree rooted at index i. 
# n is size of heap 

def heapify(A,n,i):  #строим дерево по убыванию 
    
    largest = i # Initialize largest as root 
    l = 2 * i + 1 # left index
    r= 2 * i + 2 # right index
 
    if l < n and A[i] < A[l]: #See if left child of root exists and is greater than root 
        largest = l
  
    if r < n and A[largest] < A[r]:
        largest = r
        
    if largest !=i :  # Change root, if needed 
        
        A[i], A[largest] = A[largest], A[i] #swap
        
        return heapify(A,n,largest)
                
def heapsort(A):
    
    n = len(A) # длина списка
    
    for i in range(n//2,-1,-1): #build maxheap 
        
        heapify(A,n,i)
        
    for i in range(n-1,0,-1): # One by one extract elements
        
        A[i], A[0] = A[0], A[i]
        
        heapify(A,i,0)
    return A
        
A= [ 12, 11, 13, 5, 6, 7]
print(heapsort(A))



# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapsort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i])
    
    
#----------------------------------------------------------------
# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)
        return A

# Управляющий код для тестирования
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
# Этот код предоставил Mohit Kumra
#---------------------------------------------------------
# Основной алгоритм сортировки кучей
def HeapSort(data):

    # Формируем первоначальное сортирующее дерево
    # Для этого справа-налево перебираем элементы массива
    # (у которых есть потомки) и делаем для каждого из них просейку
    for start in range((len(data) - 2) / 2, -1, -1):
        HeapSift(data, start, len(data) - 1) 

    # Первый элемент массива всегда соответствует корню сортирующего дерева
    # и поэтому является максимумом для неотсортированной части массива.
    for end in range(len(data) - 1, 0, -1): 
        # Меняем этот максимум местами с последним 
        # элементом неотсортированной части массива
        data[end], data[0] = data[0], data[end]
        # После обмена в корне сортирующего дерева немаксимальный элемент
        # Восстанавливаем сортирующее дерево
        # Просейка для неотсортированной части массива
        HeapSift(data, 0, end - 1)
    return data

# Просейка свеху вниз, в результате которой восстанавливается сортирующее дерево
def HeapSift(data, start, end):

    # Начало подмассива - узел, с которого начинаем просейку вниз
    root = start 
    
    # Цикл просейки продолжается до тех пор,
    # Пока встречаются потомки, большие чем их родитель
    while True:

        child = root * 2 + 1 # Левый потомок
        # Левый потомок за пределами подмассива - завершаем просейку
        if child > end: break 

        # Если правый потомок тоже в пределах подмассива,
        # то среди обоих потомков выбираем наибольший
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1

        # Если больший потомок больше корня, то меняем местами
        # при этом больший потомок сам становится корнем, 
        # от которого дальше опускаемся вниз по дереву
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break
        