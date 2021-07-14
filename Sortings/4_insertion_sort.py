def InsertionSort(A): 
    for i in range(1, len(A)): 
        # В new_elem сохранили значение A[i] 
        new_elem = A[i] 
        # Начиная с элемента A[i - 1] 
        j = i - 1 
        # все элементы, которые больше new_elem 
        while j >= 0 and A[j] > new_elem: 
            # сдвигаем вправо на 1 
            A[j + 1] = A[j] 
            j -= 1 
        # На свободное место записываем new_elem 
        A[j + 1] = new_elem
        
    return A
        
A=[int(i) for i in input().split()]


print(*InsertionSort(A))


# time O(N^2)
