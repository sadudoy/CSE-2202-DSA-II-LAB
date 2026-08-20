arr = [5, 3, 1, 6, 4, 2, 8, 7]

def mergeSort(arr, start, end):
    if start < end:
        middle = (start+end)//2
        mergeSort(arr, start, middle)
        mergeSort(arr, middle+1, end)
        sort(arr, start, middle, end)

def sort(arr, start, middle, end):
    left = []
    right = []

    for i in range(start, middle+1):
        left.append(arr[i])
    for i in range(middle+1, end+1):
        right.append(arr[i])
    
    i = 0
    j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

mergeSort(arr, 0, len(arr)-1)

print(arr)