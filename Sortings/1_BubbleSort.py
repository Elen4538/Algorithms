# по возрастанию       
def bubbleSort(arr): 
    n = len(arr)    
    for i in range(n):          
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] :  # если поменять знак будет по убыванию
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr
                
                
arr=[int(i) for i in input().split()]
