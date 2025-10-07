def bubble_sort_gen(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr[:]

def quick_sort_gen(arr, low=0, high=None):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            yield arr[:]
        arr[i], arr[high] = arr[high], arr[i]
        yield arr[:]
        return i

    if high is None:
        high = len(arr) - 1

    if low < high:
        partition_gen = partition(arr, low, high)
        try:
            while True:
                yield next(partition_gen)
        except StopIteration as e:
            pivot_index = e.value

        yield from quick_sort_gen(arr, low, pivot_index - 1) #sort the left part
        yield from quick_sort_gen(arr, pivot_index + 1, high) #sort the right part



def merge_sort_gen(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort_gen(arr, start, mid)
        yield from merge_sort_gen(arr, mid, end)

        left = arr[start:mid]
        right = arr[mid:end]
        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr[:]

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            yield arr[:]

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr[:]
