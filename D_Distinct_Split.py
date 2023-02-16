test = int(input())
for _ in range(test):
    size = int(input())
    string = input()
    setA = set()
    setB = set()
    flag = True
    for char in string:
        if size == 0:
            print(0)
            break
        elif flag and char not in setA:
            setA.add(char)
        elif flag and char in setA:
            setB.add(char)
            flag = False
        else:
            if char in setB:
                break
            else:
                setB.add(char)
    if size == 0:
        pass
    else:
        print(len(setA) + len(setB))