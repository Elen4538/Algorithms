
#по убыванию
def BubbleSort(A): 
    for j in range(len(A) - 1, 0, -1): 
        for i in range(0, j): 
            if A[i] > A[i + 1]: 
                A[i], A[i + 1] = A[i + 1], A[i]
                
                
         # по возрастанию       
def bubbleSort(arr): 
    n = len(arr)    
    for i in range(n):          
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                
                
arr=[int(i) for i in input().split()]