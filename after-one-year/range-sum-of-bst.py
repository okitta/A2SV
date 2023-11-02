# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def traverse(node):
            nonlocal res
            if not node:
                return
            if node.val >= low and node.val <= high:
                res += node.val
            if node.left:
                left = traverse(node.left)
            if node.right:
                right = traverse(node.right)
            return node
        traverse(root)
        return res
        