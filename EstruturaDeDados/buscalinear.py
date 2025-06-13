def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1) 
    return arr
def _quicksort(arr, left, right):
    if left < right: 
        pi = partition(arr, left, right) 
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)
def partition(arr, left, right):
    pivot = arr[right] 
    i = left - 1 

    for j in range(left, right):
        if arr[j] <= pivot: 
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def busca_linear(arr, target):
    for i in range(len(arr)):
        if arr[i] >= target:
            return i
    return len(arr)

def busca_binaria(arr, target):
    left, right = 0, len(arr) - 1  
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] >= target:
            return mid - 1
        elif arr[mid] < target: 
            left = mid + 1  
        else: 
            right = mid - 1  
    return len(arr)
    
arr1 = [3,1,2,7,6,9,4,8]
print(quicksort(arr1))

res = busca_binaria(arr1, 5)

print(f"Index com busca linear: {busca_linear(arr1, 5)}")
print(f"Index com busca binária: {res}")
