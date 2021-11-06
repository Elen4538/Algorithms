def merge(A, B):   #работа O(n) время работы линейное каждый элемент обр 1 раз
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i]) 
            i += 1 
        else:
            Res.append(B[j]) 
            j += 1 
    Res += A[i:] + B[j:]   
    return Res  

def MergeSort(A):    # O(nlogn) рекурсивная функция
    if len(A) <= 1: 
        return A 
    else:
        middle=len(A)//2
        L = A[:middle] 
        R = A[middle:] 
   
return merge(MergeSort(L), MergeSort(R))   

A=[int(s) for s in input().split()]
print(*MergeSort(A))
