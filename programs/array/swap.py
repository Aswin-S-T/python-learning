def swapArr(arr):
    if len(arr) > 0:
        last = arr[0]
        
        arr[0] = arr[-1]
        arr[-1] = last    
        return arr


arr1 = [12, 35, 9, 56, 24]
ans = swapArr(arr1)
print(ans)