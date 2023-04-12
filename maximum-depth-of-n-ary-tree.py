"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        result = 0
        def dfs(node,counter):
            nonlocal result
            if not node:
                return
            result = max(result,counter+1)
            counter += 1
            for root_node in node.children:
                dfs(root_node,counter)
        dfs(root,0)
        return result