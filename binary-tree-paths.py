# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        cur = []
        ans = []
        def helper(root, cur):    
            if not root:
                return []
            cur.append(str(root.val))
            helper(root.left, cur.copy())
            helper(root.right, cur.copy())
            if not root.left and not root.right:
                ans.append("->".join(cur))
            # return ans
        helper(root,cur)
        return  ans