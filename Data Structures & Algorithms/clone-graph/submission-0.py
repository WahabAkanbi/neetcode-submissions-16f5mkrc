"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #my intuition: first go through the graph and create every single node
        seen = {}

        queue = deque()
        queue.append(node)
        if not node:
            return None

        while queue:
            original = queue.popleft()
            clone = Node(original.val)
            seen[original] = clone
            if(original.neighbors):
                for children in original.neighbors:
                    if(children not in seen and children):
                        queue.append(children)
        
        #this is just initialization of all the nodes
        #step 2 is attaching the neighbors

        for key, value in seen.items():
            if(key.neighbors):
                neighbor = []
                for children in key.neighbors:
                    neighbor.append(seen[children])
                value.neighbors = neighbor

        return seen[node]




        