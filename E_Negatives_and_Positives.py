test = int(input())
for _ in range(test):
    size = int(input())
    arr = list(map(int,input().split()))
    left = 0
    right = 1
    max_sum = sum(arr)
    while right < size:
        arr[left] *= -1
        arr[right] *= -1
        cur_sum = sum(arr)
        if cur_sum > max_sum:
            max_sum = cur_sum
        arr[left] *= -1
        arr[right] *= -1
        left += 1
        right += 1
    print(max_sum)