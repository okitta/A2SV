test = int(input())
for _ in range(test):
    p,m = map(int,input().split())
    left = 1
    right = p+m
    counter = 0
    while left <= right:
        mid = (left+right)//2
        pro = p - mid
        mat = m - mid
        # print(pro,mat,mid)
        if pro >= 0 and mat >= 0 and pro + mat >= 2*mid:
            counter = mid
            left = mid+1            
        else:
            right = mid-1
    print(counter)