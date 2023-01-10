taste_case_numbers = int(input())
for iterator in range(taste_case_numbers):
    array_size = int(input())
    answer = 'Yes'
    given_array = list(map(int,input().split()))
    while len(given_array)>1:
        if given_array[0]>=given_array[-1]:
            large_num = given_array[0]
            given_array.pop(0)
        else:
            large_num = given_array[-1]
            given_array.pop(-1)
        if large_num <given_array[0] or large_num < given_array[-1]:
            answer = 'No'
            break
    print(answer)