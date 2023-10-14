# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def travers(node):
            if not node:
                return False, node
            if node:
                flag1, left = travers(node.left)
                flag2, right = travers(node.right)
                if node.val == p.val or node.val ==q.val:
                    return True, node
                if (flag1 and not flag2) or (not flag1 and flag2):
                    return True, left if flag1 else right
                if flag1 and flag2:
                    return True, node

            return False, node
        return travers(root)[1]