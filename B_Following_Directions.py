test = int(input())
for _ in range(test):
    size = int(input())
    string = input()
    direction = [0,0]
    counter = 0
    for i in string:
        if i == 'U':
            direction[0] += 1
            if direction == [1,1]:
                print("YES")
                break
        elif i == 'D':
            direction[0] -= 1
            if direction == [1,1]:
                print("YES")
                break
        elif i == 'R':
            direction[1] += 1
            if direction == [1,1]:
                print("YES")
                break
        else:
            direction[1] -= 1
            if direction[0] == 1 and direction[1] == 1:
                print("YES")
                break
        counter += 1
    if counter == size:
        print("NO")