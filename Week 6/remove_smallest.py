test_case = int(input())
for _ in range(test_case):
    array_size = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    counter = 0
    for index in range(array_size-1):
        if arr[index+1] - arr[index] <= 1:
            counter += 1
    if array_size - counter == 1:
        print("YES")
    else:
        print("NO")
    