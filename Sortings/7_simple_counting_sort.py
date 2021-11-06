#сортировка подсчетом

def SimpleCountingSort(A):   # без функции максимум
    scope = max(A) + 1       # O(n+k)   линейное время в лечшем случае O(n)
    C = [0] * scope
    for x in A :
        C[x] += 1
    A[:] = []
    for number in range(scope):
        A += [number] * C[number] 
