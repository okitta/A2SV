vertice = int(input())
for idx in range(vertice):
    counter = 0
    arr = []
    row = list(map(int,input().split()))
    for jdx in range(len(row)):
        if row[jdx] == 1:
            counter += 1
            arr.append(str(jdx+1))
    if counter > 1:
        print(counter," ".join(arr))
    else:
        print(1,arr[0])