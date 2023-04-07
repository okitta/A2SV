
a=int(input())
b=list(map(int,input().split()))
c=sum(i&1 for i in b)
if 0<c<a:print(*sorted(b))
else:print(*b)