class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = defaultdict(int)
        chars = "!?',;."
        for i in range(len(chars)):
            paragraph = paragraph.replace(chars[i],' ')
        
        paragraph = paragraph.lower()
        arr = paragraph.split(' ')
        # print(arr)

        for i in arr:
            if i != '':
                count[i] += 1

        sort_dict = sorted(count.items(), key=lambda y: y[1], reverse=True)

        for item in sort_dict:
            if item[0] not in banned:
                return item[0]