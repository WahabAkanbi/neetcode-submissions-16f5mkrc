class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            row_len = len(board)
            col_len = len(board[0])

            if(row_len % 3 != 0):
                return False
            if(col_len % 3 != 0):
                return False

            #check to see if row contains digits 1-9
            row_set = set()

            for row_index, row_value in enumerate(board):
            # for each row val, check if we have a  value in 1 to 9
                each_row = set()
                for value in row_value:
                    if(value == "."):
                        continue
                    
                    value = int(value)
                    if(0 < value <= 9) and (value not in each_row):
                        each_row.add(value)
                    else:
                        return False
            
            #check rows, now check colmn
            for col_index in range(col_len):
                each_col = set()
                for row_index in range(row_len):
                    value = board[row_index][col_index]
                    if(value == "."):
                        continue
                    value = int(value)
                    if (0 < value <= 9) and (value not in each_col):
                        each_col.add(value)
                    else:
                        return False
                                                                                                                                                                                                                                                                                                        
            def last_check(start_row, start_col):
                seen_box = set()
                for row_index in range(start_row, start_row + 3):
                    for col_index in range(start_col, start_col + 3):
                        value = board[row_index][col_index]
                        if(value == "."):
                            continue
                        value = int(value)
                        if (0 < value <= 9) and (value not in seen_box):
                            seen_box.add(value)
                        else:
                            return False
                return True
            #Call last check with every row
            #total starts and end we will have
            total_row = row_len // 3
            total_col = col_len // 3

            for row_index in range(total_row):
                for col_index in range(total_col):
                    start_row = row_index * 3
                    start_col = col_index * 3
                    if(not last_check(start_row, start_col)):
                        return False
            
            return True
                








                                                                                                                                                                                                                                                                                                                                    