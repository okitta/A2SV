class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = {i:i for i in range(len(s))}
        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        for pair in pairs:
            px = find(pair[0])
            py = find(pair[1])
            
            if px != py:
                rep[py] = px
        index = defaultdict(list)
        letter = defaultdict(list)

        for key,values in rep.items():
            index[find(values)].append(key)
            letter[find(values)].append(s[key])
        for key in index.keys():
            index[key].sort()
            letter[key].sort()

        ans = list(s)

        for key in index.keys():
            for i in range(len(index[key])):
                ans[index[key][i]] = letter[key][i]
        return "".join(ans)