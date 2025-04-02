def search(arr,n,x):
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1

arr = [1,3,7,9,5,0]
n = len(arr)
x = 5

result = search(arr,n,x)
if result == -1:
    print("element not found")
else:
    print("element found at index", result)