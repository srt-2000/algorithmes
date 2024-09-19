def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[int(len(arr)/2)]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

a = [2, 4, 1, 6, 7, 9, 11, 12]
print(quick_sort(a))
