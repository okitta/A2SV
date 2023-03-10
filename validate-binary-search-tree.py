# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,arr):
        def helper(node):
            if node:
                helper(node.left)
                arr.append(node.val)
                helper(node.right)
        helper(node)
        return arr

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.inorder(root,[])
        return ans == sorted(ans) and len(set(ans)) == len(ans)