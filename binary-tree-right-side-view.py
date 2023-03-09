# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(list)
        ans = []

        def breadth_first(root,level):
            if not root:
                return
            dic[level].append(root.val)
            breadth_first(root.left,level+1)
            breadth_first(root.right,level+1)
        breadth_first(root,0)
        for items in dic:
            ans.append(dic[items][-1])
        return ans