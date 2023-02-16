arr_size1,arr_size2 = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1_pointer = 0
arr2_pointer = 0
arr = []
while arr1_pointer < arr_size1 and arr2_pointer < arr_size2:
    if arr1[arr1_pointer] < arr2[arr2_pointer]:
        arr.append(arr1[arr1_pointer])
        arr1_pointer += 1
    else:
        arr.append(arr2[arr2_pointer])
        arr2_pointer += 1
if arr1_pointer < arr_size1:
    for index in range(arr1_pointer,arr_size1):
        arr.append(arr1[index])
elif arr2_pointer < arr_size2:
    for index in range(arr2_pointer,arr_size2):
        arr.append(arr2[index])
print(*arr)