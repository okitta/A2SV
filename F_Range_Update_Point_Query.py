def digit(x):
    sum_dic = {}
    # arr = []
    # print(x)
    for item in x:
        sum_digit = 0
        number = str(item)
        for char in number:
            sum_digit += int(char)
        sum_dic.update({item:sum_digit})
    return sum_dic
test = int(input())
for _ in range(test):
    size, query = map(int,input().split())
    arr = list(map(int,input().split()))
    for n in range(query):
        given = list(map(int,input().split()))
        sum_dic = digit(arr)
        # print(sum_dic)
        if given[0] == 1:
            for idx in range(given[1]-1 , given[2]):
                arr[idx] = sum_dic[arr[idx]]
        else:
            print(arr[given[1]-1])
