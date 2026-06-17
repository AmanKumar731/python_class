def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        # Assume current index minimum hai
        min_index = i

        # Remaining array me smallest find karo
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap smallest with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [5, 3, 8, 4, 2]
print(selection_sort(arr))