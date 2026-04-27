from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        row_len = len(grid)
        col_len = len(grid[0])
        land = pow(2, 31) -1
        queue = deque()

        def bfs():
            while queue:
                row, col = queue.popleft()
                for dx, dy in directions:
                    rdx = row + dx
                    cdy = col + dy

                    if((0 <= rdx<row_len) and (0<=cdy<col_len)):
                        if((grid[rdx][cdy] == land)):
                            #if we are equal to inf then we want to find the delta from original location
                            grid[rdx][cdy] = grid[row][col] + 1
                            queue.append((rdx, cdy))

        #Put all the 0's into the queue
        for row_id, row_val in enumerate(grid):
            for col_id, col_val in enumerate(row_val):
                if(col_val == 0):
                    queue.append((row_id, col_id))
        
        bfs()

        return None
        