def getMinMax( a, n):
    min_val = a[0]
    max_val = a[0]
    
    for i in range(n):
        if a[i] < min_val:
            min_val = a[i]
        elif a[i] > max_val:
            max_val = a[i]
            
    return min_val, max_val

arr = [1,4,2,12,56,3,0]
n = len(arr)
print(getMinMax(arr, n))
