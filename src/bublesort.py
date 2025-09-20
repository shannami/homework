def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [4, 90, 6, 14, 35, 7]
buble_sort(arr)
print(arr) 

