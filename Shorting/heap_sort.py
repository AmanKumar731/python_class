import heapq

def heap_sort(arr):

    # List ko heap me convert karo
    heapq.heapify(arr)

    sorted_arr = []

    # Smallest element nikalte jao
    while arr:
        sorted_arr.append(heapq.heappop(arr))

    return sorted_arr

arr = [5, 3, 8, 4, 2]
print(heap_sort(arr))