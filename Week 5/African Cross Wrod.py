no_row,no_col = map(int,input().split())
given_matrix = []
row_arr = set()
col_arr = set()
ans = ''
for row in range(no_row):
    given_matrix.append(list(map(str,input())))
for row in range(no_row):
    for col in range(no_col):
        row_counter = 0
        col_counter = 0
        row_pointer = 0
        col_pointer = 0
        item = given_matrix[row][col]
        while row_pointer < no_row:
            if given_matrix[row_pointer][col] == item:
                col_counter += 1
            row_pointer += 1
        while col_pointer < no_col:
            if given_matrix[row][col_pointer] == item:
                row_counter += 1
            col_pointer += 1
        if row_counter > 1:
            row_arr.add(f"for {item} in row {row}")
        if col_counter > 1:
            col_arr.add(f"for {item} in col {col}")
for row in range(no_row):
    for col in range(no_col):
        item = given_matrix[row][col]
        key_row = f"for {item} in row {row}"
        key_col = f"for {item} in col {col}"
        if key_col in col_arr or key_row in row_arr:
            pass
        else:
            ans += item
print(ans)