def quick_sort(s):
    if len(s) <= 1 :
        return (s)
    
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))
    
    
    return quick_sort(left) + center + quick_sort(right)

s = [int(i) for i in input().split()]
print (quick_sort(s))

array = [29,19,47,11,6,19,24,12,17,23,11,71,41,36,71,13,18,32,26]
print (quick_sort(array))

#Time - NlogN
