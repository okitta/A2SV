# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def average(node):
            nonlocal count
            if node:
                average(node.left)
                average(node.right)

                node.total, node.nodes = node.val, 1

                if node.left:
                    node.total += node.left.total
                    node.nodes += node.left.nodes

                if node.right:
                    node.total += node.right.total
                    node.nodes += node.right.nodes

                if node.val == int(node.total / node.nodes):
                    count += 1

        average(root)

        return count