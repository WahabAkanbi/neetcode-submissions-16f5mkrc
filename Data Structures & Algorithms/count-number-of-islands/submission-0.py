from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count_island = 0
        row_length = len(grid)
        col_length = len(grid[0])
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]

        def bfs(row_id, col_id):
            queue = deque()
            queue.append((row_id, col_id))
            seen.add((row_id, col_id))


            while queue:
                row_id, col_id = queue.popleft()
                for dx, dy in directions:
                    nrow_id = row_id + dx
                    ncol_id = col_id + dy
                    if(0 <= nrow_id < row_length) and (0<= ncol_id < col_length):
                        if(grid[nrow_id][ncol_id] == "1") and (nrow_id, ncol_id) not in seen:
                            seen.add((nrow_id, ncol_id))
                            queue.append((nrow_id, ncol_id))


        #iterate through all the island
        for row_id, row_val in enumerate(grid):
            for col_id, col_val in enumerate(row_val):
                if(col_val == "1"):
                    if((row_id, col_id) not in seen):
                        count_island += 1
                        bfs(row_id, col_id)

        return count_island
        