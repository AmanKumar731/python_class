def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Array ko do parts me divide karo
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    # Dono sorted arrays ko merge karo
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Remaining elements add karo
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [5, 3, 8, 4, 2]
print(merge_sort(arr))