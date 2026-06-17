def counting_sort(arr):

    # Maximum value find karo
    max_val = max(arr)

    # Count array banao
    count = [0] * (max_val + 1)

    # Frequency count karo
    for num in arr:
        count[num] += 1

    result = []

    # Sorted array rebuild karo
    for i in range(len(count)):
        result.extend([i] * count[i])

    return result

arr = [5, 3, 8, 4, 2]
print(counting_sort(arr))