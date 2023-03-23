from bisect import *
items= int(input())
names = list(map(str,input().split(' ')))
insert = int(input())
insert_names = []
for i in range(insert):
    insert_names.append(input())
for name in insert_names:
    print(bisect_left(names,name))