arr_size,element = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
if len(arr)>1 and arr[element-1] != arr[element]:
    print(arr[element-1])
else:
    if arr[element-1] - 1 > 0 and element == 0:
        print(arr[element-1]-1)
    else:
        print(-1)