# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def bfs(node):
            queue = deque()
            queue.append(root)

            while queue:
                result = []
                for _ in range(len(queue)):
                    nd = queue.popleft()
                    if(nd):
                        if(nd.left):
                            queue.append(nd.left)
                        if(nd.right):
                            queue.append(nd.right)
                        result.append(nd.val)
                if(len(result) >= 1):
                    output.append(result)
                
        bfs(root)
        return output
        