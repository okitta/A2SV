test = int(input())
for _ in range(test):
    string = input()
    min_len = len(string)
    arr = [-1,-1,-1]
    if '1' not in string or'2' not in string or '3' not in string:
        min_len = 0
    else:    
        for item in range(len(string)):
            arr[int(string[item])-1] = item
            if -1 not in arr:
                max_ind = max(arr)
                min_ind = min(arr)
                min_len = min(min_len,max_ind-min_ind+1)
    print(min_len)