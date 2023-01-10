# Enter your code here. Read input from STDIN. Print output to STDOUT
main_set = set(input().split(' '))
flag = True
for iterator in range(int(input())):
    check_set = set(input().split(' '))
    if check_set.issubset(main_set) and len(main_set-check_set) >=1:
        pass
    else:
        flag = False
        break
print(flag)