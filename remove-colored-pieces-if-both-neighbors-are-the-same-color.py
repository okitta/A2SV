class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        dic = {"A":0,"B":0}
        for i in range(len(colors)):
            if i+3 <= len(colors) and len(set(colors[i:i+3])) == 1:
                if "A" in set(colors[i:i+3]):
                    dic["A"] += 1
                else:
                    dic["B"] += 1
        # print(dic)
        if dic["B"] < dic["A"]:
            return True
        return False