# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return -1
            if(not node.left) and (not node.right):
                return node.val


            left_sub = dfs(node.left)
            right_sub = dfs(node.right)

            temp = node.left
            node.left = node.right
            node.right = temp

        dfs(root)
        return root
        