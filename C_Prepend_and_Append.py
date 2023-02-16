test = int(input())
for _ in range(test):
    size = int(input())
    string = input()
    left_pointer =0
    right_pointer = size-1
    while left_pointer <= right_pointer:
        if string[left_pointer] == '0' and string[right_pointer] == '1':
            left_pointer += 1
            right_pointer -= 1
        elif string[left_pointer] == '1' and string[right_pointer] == '0':
            left_pointer += 1
            right_pointer -= 1
        else:
            print(right_pointer - left_pointer + 1)
            break
    if left_pointer > right_pointer:
        print(0)