
test_case = int(input())
for _ in range(test_case):
    row,col = map(int,input().split())
    fdiagonal = [0 for index in range(row+col)]
    gdiagonal = [0 for index in range(row+col)]
    arr_row = []
    for row_i in range(row):
        arr_row.append(list(map(int,input().split())))
        for col_i in range(col):
            fdiagonal[row_i + col_i] += arr_row[row_i][col_i]
            gdiagonal[row_i - col_i + col] += arr_row[row_i][col_i]
    
    max_sum = 0
    for row_i in range(row):
        for col_i in range(col):
            max_sum = max(max_sum,fdiagonal[row_i + col_i] + gdiagonal[row_i - col_i + col] - arr_row[row_i][col_i])
    print(max_sum)