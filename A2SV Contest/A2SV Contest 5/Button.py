n = int(input()) 
for _ in range(n):
    malstring = input()
    answer = []
    N = len(malstring)
    if N < 2:
        print(malstring)
        continue
    current = 0
    lookahead = 0
    while lookahead < N:
        while lookahead < N and malstring[current] == malstring[lookahead]:
            lookahead += 1
        if (lookahead-current) % 2 != 0:
            answer.append(malstring[current])
        current = lookahead
    answer = sorted(list(set(answer)))
    print(''.join(answer))