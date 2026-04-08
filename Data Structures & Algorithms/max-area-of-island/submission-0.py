from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        row_len = len(grid)
        col_len = len(grid[0])
        max_count = 0

        def bfs(row_id, col_id):
            queue = deque()
            queue.append((row_id, col_id))
            seen.add((row_id, col_id))
            count = 1

            while queue:
                row_num, col_num = queue.popleft()

                for dx, dy in directions:
                    row_dx = row_num + dx
                    col_dy = col_num + dy

                    if(0 <=row_dx<row_len) and (0 <=col_dy <col_len):
                        if(grid[row_dx][col_dy] == 1) and ((row_dx, col_dy) not in seen):
                            queue.append((row_dx, col_dy))
                            seen.add((row_dx, col_dy))
                            count += 1
                
            return count

        for row_id, row_val in enumerate(grid):
            for col_id, col_val in enumerate(row_val):
                if(col_val == 1) and ((row_id, col_id) not in seen):
                    count = bfs(row_id, col_id)
                    max_count = max(count, max_count)
        
        return max_count
        
        