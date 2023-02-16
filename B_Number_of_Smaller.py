arr_size1,arr_size2 = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1_pointer = 0
arr2_pointer = 0
arr = []
counter = 0
while arr2_pointer < arr_size2:
    while arr1_pointer < arr_size1 and arr2[arr2_pointer] > arr1[arr1_pointer]:
        arr1_pointer += 1
        counter+= 1
    # print(arr2_pointer)
    arr.append(counter)
    arr2_pointer += 1
print(*arr)