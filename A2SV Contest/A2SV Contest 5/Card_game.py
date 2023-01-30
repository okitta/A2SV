arr_size = int(input())
arr = list(map(int,input().split()))
left = 0
right = arr_size - 1
wub = 0
hen = 0
while left < right:
    if arr[left] > arr[right]:
        wub += arr[left]
        left += 1
        if arr[left] > arr[right]:
            hen += arr[left]
            left += 1
        else:
            hen += arr[right]
            right -= 1
            
    else:
        wub += arr[right]
        right -= 1
        if arr[left] > arr[right]:
            hen += arr[left]
            left += 1
        else:
            hen += arr[right]
            right -= 1
if left == right:
    wub += arr[right]
print(wub,hen)