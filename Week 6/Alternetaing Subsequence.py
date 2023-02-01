test = int(input())
for _ in range(test):
    arr_size = int(input())
    arr= list(map(int,input().split()))
    temp = []
    temp.append(arr[0])
    max_sum = 0
    flag = False
    for item in arr[1:]:
        if temp[-1] > 0:
            if item < 0:
                max_sum += max(temp)
                temp.clear()
                flag = True
        else:
            if item > 0:
                max_sum += max(temp)
                temp.clear()
                flag = True
        temp.append(item)
    max_sum += max(temp)
    if flag:
        print(max_sum)
    else:
        print(max(arr))