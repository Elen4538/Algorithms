#сортировка подсчетом
def maxi(A):
    maximus=0
    for i in range(0,len(A)-1):   # функция максимум
        for i in range(i,len(A)-1):
            if A[i] > A[i+1]:
                maximus=A[i]

    return(maximus)
-----------------------------------------------------------------
def SimpleCountingSort(A):
    
    size = maxi(A) + 1    с функцией максимум
    C = [0] * size
    for x in A:
        C[x] += 1
    A[:] = []
    for number in range(size):
        A += [number] * C[number] 
        
        
    return A
        
        
A=[int(s) for s in input().split()]

SimpleCountingSort(A)
print(*A)

--------------------------------------
def SimpleCountingSort(A):   # без функции максимум
    scope = max(A) + 1  # O(n+k)   линейное время в лечшем случае O(n)
    C = [0] * scope
    for x in A :
        C[x] += 1
    A[:] = []
    for number in range(scope):
        A += [number] * C[number] 