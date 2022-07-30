
def binarySearch(alist, item):
	    first = 0 #индекс первого элемента
	    last = len(alist)-1#индекс последнего элемента
	    found = False
	
	    while first<=last and not found:#индексы
	        midpoint = (first + last)//2 #ищем середину списка- индекс
	        if alist[midpoint] == item:# если средний элемент в списке равен искомому то ОК
	            found = True
	        else:
	            if item < alist[midpoint]:#если искомое меньше среднего элемента
	                last = midpoint-1 # то сдвигаем границу поиска
	            else:
	                first = midpoint+1#наоборот то в правой 
	
	    return found
	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
 
 #время работы O(logN)
 
