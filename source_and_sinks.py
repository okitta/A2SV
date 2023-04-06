from collections import defaultdict

vertice = int(input())
source = set()
sink = set()
for idx in range(1,vertice+1):
    row = list(map(int,input().split()))
    if sum(row) > 0:
        source.add(idx)
    for jdx in range(1,len(row)+1):
        if row[jdx-1] == 1:
            sink.add(jdx)
source_result = []
sink_result = []

for i in range(1,vertice+1):
    if i in sink and i not in source:
        sink_result.append(str(i))
    elif i not in sink and i not in source:
         source_result.append(str(i))
         sink_result.append(str(i))
    elif i not in sink and i in source:
        source_result.append(str(i))

print(len(source_result), ' '.join(source_result))
print(len(sink_result), ' '.join(sink_result))