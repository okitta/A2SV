testcase = int(input())
for _ in range(testcase):
    first_sides = list(map(int,input().split()))
    second_sides = list(map(int,input().split()))
    max_side = max(first_sides)
    if max_side not in second_sides:
        print('No')
    else:
        first_sides.remove(max_side)
        second_sides.remove(max_side)
        if first_sides[0] + second_sides[0] == max_side:
            print('Yes')
        else:
            print('No')