def heapify(arr, n, i, reverse):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and (arr[l] > arr[largest] if not reverse else arr[l] < arr[largest]):
        largest = l
    if r < n and (arr[r] > arr[largest] if not reverse else arr[r] < arr[largest]):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, reverse)


def heap(arr, reverse=False):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, reverse)
