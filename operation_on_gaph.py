from collections import defaultdict
vertice = int(input())
operation = int(input())

graph = defaultdict(list)


for idx in range(operation):
    val = list(map(int,input().split()))
    if val[0] == 1:
        graph[val[1]].append((str(val[2])))
        graph[val[2]].append((str(val[1])))
    else:
        print(' '.join(graph[val[1]]))