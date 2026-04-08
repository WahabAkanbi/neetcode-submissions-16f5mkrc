# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if(not node):
                return None
    
            l_sub = dfs(node.left)
            r_sub = dfs(node.right)

            if(node.val == p.val) or (node.val == q.val):
                return node

            if(l_sub) and (r_sub):
                return node
            elif(l_sub):
                return l_sub
            else:
                return r_sub

        return dfs(root)
        