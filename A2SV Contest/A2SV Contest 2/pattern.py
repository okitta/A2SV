test = int(input())
arr = []
for _ in range(test):
    arr.append(input())
ans = []
for i in range(len(arr[0])):
    temp = set()
    for word in arr:
        temp.add(word[i])
    temp.discard('?')
    if len(temp)>1:
        ans.append('?')
    elif len(temp)==0:
        ans.append('x')
    else:
        ans.append(temp.pop())
print("".join(ans))