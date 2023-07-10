# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(node):
            nonlocal result
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_max = max(left_max,0)
            right_max = max(right_max,0)

            result = max(result,node.val+left_max+right_max)

            return node.val + max(left_max,right_max)
        dfs(root)
        return result