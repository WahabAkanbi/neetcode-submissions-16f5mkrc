# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def SameTree(nodeA, nodeB):
            if(not nodeA) and (not nodeB):
                return True
            
            if(not nodeA) and nodeB:
                return False
            
            if(not nodeB) and nodeA:
                return False

            
            l_sub = SameTree(nodeA.left, nodeB.left)
            r_sub = SameTree(nodeA.right, nodeB.right)

            if ((l_sub and r_sub) == False):
                return False

            if(nodeA.val == nodeB.val):
                return True
            else:
                return False

        return (SameTree(p, q))
        