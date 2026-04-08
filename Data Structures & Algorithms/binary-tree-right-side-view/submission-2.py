# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #using BFS and going to keep the nodes that are on the right for each level
        output = []
        def bfs(node):
            queue = deque()
            queue.append(node)
            #for each level means we iterate through len of queue

            while queue:
                level_size = len(queue)
                for index in range(level_size):
                    #if it has a right or left child then add it to the queue
                    node = queue.popleft()
                    if(node):
                        if(node.left):
                            queue.append(node.left)
                        if(node.right):
                            queue.append(node.right)
                        #record we at the right most
                        if(index == (level_size -1)):
                            output.append(node.val)

        bfs(root)
        return output


        