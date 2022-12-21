import sys
dicti = {}
k = sys.stdin
for word in k:
    dicti[word.strip()] = dicti.get(word.strip(),0)+1
result = list(dicti.values())
print(len(result[1:]))
print(' '.join(str(e) for e in result[1:]))