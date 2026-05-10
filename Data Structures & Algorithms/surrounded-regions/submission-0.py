from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row_index = len(board)
        col_index = len(board[0])
        queue = deque()

        #add all the edge pieces that ate 'O'
        for row_id in range(row_index):
            if(board[row_id][0] == "O"):
                board[row_id][0] = "S"
                queue.append((row_id, 0))
            if(board[row_id][col_index-1] == "O"):
                board[row_id][col_index-1] = "S"
                queue.append((row_id, col_index-1))
        
        for col_id in range(1, col_index):
            if(board[0][col_id] == "O"):
                board[0][col_id] = "S"
                queue.append((0, col_id))
            if(board[row_index-1][col_id] == "O"):
                board[row_index-1][col_id] = "S"
                queue.append((row_index-1, col_id))
        
        #queue should contain it all now
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        while queue:
            row_id, col_id = queue.popleft()
            for dx, dy in directions:
                d_row = dx + row_id
                d_col = dy + col_id
                if(0<=d_row< row_index) and (0<=d_col < col_index):
                    if(board[d_row][d_col] == "O"):
                        board[d_row][d_col] = "S"
                        queue.append((d_row, d_col))
        
        for row_id in range(len(board)):
            for col_id in range(len(board[0])):
                if(board[row_id][col_id] == "O"):
                    board[row_id][col_id] = "X"
                
                if(board[row_id][col_id] == "S"):
                    board[row_id][col_id] = "O"
        


        