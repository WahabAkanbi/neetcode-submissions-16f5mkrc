# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node):
            if(not node):
                return (0,-float('inf'))

            left_max, best_left = recurse(node.left)
            right_max, best_right  = recurse(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            donotsplit = max(left_max, right_max) + node.val
            split = left_max + right_max + node.val
            
            best_path = max(max(best_left, best_right), split)

            return (donotsplit, best_path)

        nosplit, best_path = recurse(root)
        return best_path