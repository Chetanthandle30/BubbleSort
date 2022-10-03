def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


a = [4, 1, 10, 2, 8, 3, 9, 5, 6, 7, 0]
sorted = bubblesort(a)
print(sorted)
