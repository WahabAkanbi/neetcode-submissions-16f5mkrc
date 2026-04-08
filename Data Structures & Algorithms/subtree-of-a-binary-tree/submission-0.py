# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(node, subnode):
            if(not node and not subnode):
                return True
            if( not node or not subnode):
                return False
            
            if(node.val != subnode.val):
                return False
    
            l_sub = sameTree(node.left, subnode.left)
            r_sub = sameTree(node.right, subnode.right)

            return l_sub and r_sub

        
        if not root:
            return False

        #with each root, check to see if the start of subtree
        if sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        

        