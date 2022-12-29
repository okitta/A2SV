# Enter your code here. Read input from STDIN. Print output to STDOUT
range1,range2 = list(map(int,input().split()))
list_1 = [input() for iterator in range(range1)]
list_2 = [input() for iterator in range(range2)]
indexed_list = [(index,value) for index,value in enumerate(list_1)]
# print(indexed_list)
# print(list_1,list_2)
for iterator in list_2:
    new_list = []
    for item in indexed_list:
        if item[1] == iterator:
            # print(item[1])
            new_list.append(str(item[0]+1))
    # print(new_list)
    if new_list:
        print(' '.join(new_list))
    else:
        print(-1)