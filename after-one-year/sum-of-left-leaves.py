# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        def traverse(node):
            nonlocal total
            if not node:
                return
            if node.left:
                left = traverse(node.left)
                if not left.left and not left.right:
                    total += left.val
            if node.right:
                right = traverse(node.right)
            
            return node
        traverse(root)
        return total