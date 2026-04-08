# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            if(not node):
                return 0
            
            l_depth = dfs(node.left)
            r_depth = dfs(node.right)

            return (max(l_depth, r_depth)+1)



        max_depth = dfs(root)
        return max_depth
        