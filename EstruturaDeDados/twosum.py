arr1 = [2,7,11,15]
arr2 = [3,2,4]

def two_sum1(alvo, arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == alvo:
                return [i, j]
def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j][0] <= pivot[0]:  
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def two_sum2(nums, target):
    arr = [(nums[i], i) for i in range(len(nums))]

    quicksort(arr)

    i = 0
    j = len(arr) - 1
    while i < j:
        soma = arr[i][0] + arr[j][0]
        if soma == target:
            return [arr[i][1], arr[j][1]]
        elif soma < target:
            i += 1
        else:
            j -= 1

def two_sum3(arr, alvo):
    indice_por_valor = {}  

    for i, valor_atual in enumerate(arr):
        complemento = alvo - valor_atual
        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        indice_por_valor[valor_atual] = i
  
alvo = 9
alvo2 = 6

r = two_sum1(alvo, arr1)
r2 = two_sum2(arr2, alvo2)
r3 = two_sum3(arr1, alvo)

print(r)
print(r2)
print(r3)
