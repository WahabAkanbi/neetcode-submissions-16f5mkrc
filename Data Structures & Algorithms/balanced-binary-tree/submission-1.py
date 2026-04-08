# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if(not node):
                return (0, True)


            
            l_depth, l_bal = dfs(node.left)
            r_depth, r_bal = dfs(node.right)

            n_depth = (max(l_depth, r_depth) + 1)
            n_balance = (abs(l_depth - r_depth) <= 1) and l_bal and r_bal

            return(n_depth, n_balance)

        return(dfs(root)[1])
        