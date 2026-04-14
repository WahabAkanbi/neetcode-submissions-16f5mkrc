# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def recurse(node):
            if(not node):
                return None

            if(node.val == p.val) or (node.val == q.val):
                return node

            left_sub = recurse(node.left)
            right_sub = recurse(node.right)

            if(left_sub) and (right_sub):
                return node
            elif left_sub:
                return left_sub
            elif right_sub:
                return right_sub
            return None


        return recurse(root)
        