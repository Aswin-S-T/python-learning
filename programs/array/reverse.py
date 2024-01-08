def reverseArr(arr):
    if (len(arr) > 0):
        first = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
            
        arr[len(arr) -1] = first
        return arr
            
list = [4, 5, 6, 7, 8, 9]
ans = reverseArr(list)
print(ans)