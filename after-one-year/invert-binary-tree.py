# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def travers(node):
            if not node:
                return
            node.right,node.left = travers(node.left),travers(node.right)

            return node
        travers(root)
        return root

        