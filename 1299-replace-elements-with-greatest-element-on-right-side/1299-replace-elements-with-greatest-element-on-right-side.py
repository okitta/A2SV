class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        max_num = arr[-1] 
        for item in range(len(arr)-1,-1,-1):
            if len(arr) == 1:
                ans.append(-1)
            elif len(ans) < len(arr):
                if arr[item] > max_num:
                    max_num = arr[item]
                    ans.append(arr[item])
                elif item == len(arr)-1:
                    ans.append(-1)
                    ans.append(arr[item])
                else:
                    ans.append(max_num)
        ans.reverse()
            
#         for item in range(len(arr)):
#             num = arr[item+1:]
#             if item == len(arr)-1:
#                 ans.append(-1)
#             else:
#                 ans.append(max(num))
        return ans
        