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



# Driver
arr = [ 12, 11, 13, 5, 6, 7] 
heapsort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i])
    
