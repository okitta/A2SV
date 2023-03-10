# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequent = defaultdict(int)
        result = []
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                frequent[root.val]+=1
        helper(root)
        sorted_freq = dict(sorted(frequent.items(), key=lambda item: item[1],reverse=True))
        for key,value in sorted_freq.items():
            if not result or sorted_freq[result[-1]] == value:
                result.append(key)
            else:
                break
        return result