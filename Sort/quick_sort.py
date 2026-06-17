def quick_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Middle element ko pivot banao
    pivot = arr[len(arr)//2]

    # Pivot se chote elements
    left = [x for x in arr if x < pivot]

    # Pivot ke equal elements
    middle = [x for x in arr if x == pivot]

    # Pivot se bade elements
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 3, 8, 4, 2]
print(quick_sort(arr))