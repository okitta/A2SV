# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def travers(node,arr):
            if not node:
                return
            arr.append(node.val)
            if node.right:
                right = travers(node.right,arr)
                # arr.append(right.val)
            if node.left:
                left = travers(node.left,arr)
                # arr.append(left.val)
            return node
        travers(root,arr)
        arr.sort()
        # print(arr)
        node = TreeNode()
        def new_tree(node,idx,arr):
            if idx == len(arr):
                return
            node = TreeNode(arr[idx])
            node.right = new_tree(node,idx+1,arr)
            # node.left = Tree()
            return node
        tree = new_tree(node,0,arr)
        return tree

