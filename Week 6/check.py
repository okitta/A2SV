test_case = int(input())
for _ in range(test_case):
    arr_size = int(input())
    arr = list(map(int,input().split()))
    max_sum = 0
    temp = []
    pointer = 0
    temp.append(arr[0])
    while pointer < arr_size:
        if temp[-1] > 0:
            if arr[pointer] > 0:
                 temp.append(arr[pointer])
                 temp.sort()
            else:
                max_sum += temp[-1]
                temp = []
        else:
            if arr[pointer] < 0:
                 temp.append(arr[pointer])
                 temp.sort()
            else:
                max_sum += temp[-1]
                temp = []
    print(max_sum)
                 