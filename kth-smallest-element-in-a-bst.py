# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def items(self,root,ans):
        def helper(root):
            if root:
                helper(root.left)
                ans.append(root.val)
                helper(root.right)
            return ans
        return helper(root)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = self.items(root,[])
        return ans[k-1]