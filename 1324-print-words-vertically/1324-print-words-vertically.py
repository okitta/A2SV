class Solution:
    def printVertically(self, s: str) -> List[str]:
        check_list = s.split(' ')
        size = len(check_list)
        # print(check_list)
        max_len = 0
        for item in check_list:
            if len(item) > max_len:
                max_len = len(item)
        check = [""]*max_len
        for word in check_list:
            for index in range(len(check)):
                if index < len(word):
                    check[index] += word[index]
                else:
                    check[index] += " "
        check2 = []
        for word in check:
            check2.append(word.rstrip())
        return check2