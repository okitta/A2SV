# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        delete = set(to_delete)

        def dfs(node):
            if node is None:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in delete:
                if node.left is None and node.right is None:
                    return None
                else:
                    if node.left:
                        # print(node.left.val)
                        ans.append(node.left)
                    if node.right:
                        ans.append(node.right)
                    return None
            return node

        initial = dfs(root)
        if initial:
            ans.append(initial)
        return ans