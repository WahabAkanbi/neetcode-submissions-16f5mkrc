from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #add all the rotten fruits to the queue initially
        queue = deque()
        #added all the rotten items to queue
        total = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for row_id, row_val in enumerate(grid):
            for col_id, col_val in enumerate(row_val):
                if(col_val == 2):
                    queue.append((row_id, col_id))
                elif(col_val == 1):
                    total += 1
        if(total == 0):
            return 0
        #we will go round by round
        minute = 0
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        while queue:
            for rounds in range(len(queue)):
                row_id, col_id = queue.popleft()
                for dx, dy in directions:
                    d_row = dx + row_id
                    d_col = dy + col_id

                    if(0<=d_row<row_len) and (0<=d_col<col_len):
                        if(grid[d_row][d_col] == 1):
                            total -= 1
                            grid[d_row][d_col] = 2
                            queue.append((d_row, d_col))
            if(queue):
                minute += 1
        
        if(total > 0):
            return -1
        else:
            return minute



        