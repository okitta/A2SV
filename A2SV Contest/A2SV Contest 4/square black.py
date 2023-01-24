row,col = list(map(int,input().split()))
min_col = col
min_row = row
max_col = 1
max_row = 1
counter = 0
for index in range(1,row+1):
    given_string= input()
    bcount = given_string.count('B')
    if 'B' in given_string:
        counter +=bcount
    if (given_string.find('B') + 1) > max_col:
        max_col = (given_string.find('B') + 1)
    if (given_string.find('B') + 1) != 0  and (given_string.find('B') + 1) < min_col:
        min_col = (given_string.find('B') + 1)
    if (given_string.find('B') + 1) != 0 and index > max_row:
        max_row = index
    if (given_string.find('B') + 1) != 0 and index < min_row:
        # print(index)
        min_row = index
max_area = max((max_row-min_row+1),(max_col-min_col+1))
if max_area > row or max_area > col:
    print(-1)
else:
    print((max_area**2) - counter)
    
    
            
        