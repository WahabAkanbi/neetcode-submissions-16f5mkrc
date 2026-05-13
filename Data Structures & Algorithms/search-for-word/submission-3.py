class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])
        word_len = len(word)
        seen = set()
        directions = [(1,0), (0,1), (-1,0), (0, -1)]
        #find letter then choose the letter, check all 4 directions to see if 
        # we find a match kind of like BFS

        result = [False]
        def recurse(row_id, col_id, word_id):
            if(word_id == word_len):
                return True
            if((row_id, col_id)) in seen:
                return False

            if(0<=row_id<row_len) and (0<=col_id <col_len) and (word_id< word_len):
                if(board[row_id][col_id] == word[word_id]):
                    seen.add((row_id, col_id))
                    #try to go all 4 directions
                    for dx, dy in directions:
                        r_dx = row_id + dx
                        c_dy = col_id + dy
                        result[0] |= recurse(r_dx, c_dy, word_id + 1)
                    seen.remove((row_id, col_id))
            return result[0]
        
        for row_index, row_val in enumerate(board):
            for col_index, col_val in enumerate(row_val):
                if(col_val == word[0]):
                    #call bfs with curr row, curr col and also index 0 of word
                    recurse(row_index, col_index, 0)
        
        return result[0]


        