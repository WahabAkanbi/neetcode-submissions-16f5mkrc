# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if(not node):
                return 0

            l_sub = dfs(node.left)
            r_sub = dfs(node.right)
            
            #at each node, diameter is longest path through its left and right subtree
            diameter = max(diameter, l_sub + r_sub)
            #return the depth upward
            return (max(l_sub, r_sub) + 1)

        dfs(root)
        return diameter
        