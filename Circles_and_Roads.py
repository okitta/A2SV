vertice = int(input())
counter = 0

for idx in range(vertice):
    row = list(map(int,input().split()))
    for jdx in range(len(row)):
        if row[jdx] == 1:
            counter += 1
print(counter // 2)