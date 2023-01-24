given_inputs = int(input())
positive = []
negative = []
zero = []
given_arr = list(map(int,input().split()))
for items in given_arr:
    if items > 0:
        positive.append(items)
    elif items < 0:
        negative.append(items)
    else:
        zero.append(items)
if len(negative)%2 == 0:
    item = negative.pop()
    zero.append(item)
if len(negative) > 2 and len(positive) == 0:
    item1 = negative.pop()
    item2 = negative.pop()
    positive.append(item1)
    positive.append(item2)
print(len(negative),end =" ")
for items in negative:
    print(items,end =" ")
print(" ")
print(len(positive),end =" ")
for items in positive:
    print(items,end =" ")
print(" ")
print(len(zero),end =" ")
for items in zero:
    print(items,end =" ")