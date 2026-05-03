class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose first

        #since in place use range(len)
        for row_index in range(len(matrix)):
            for col_index in range(row_index+ 1, len(matrix[0])):
                temp = matrix[row_index][col_index]
                matrix[row_index][col_index] = matrix[col_index][row_index]
                matrix[col_index][row_index] = temp

        #reverse each row:

        for row_index in range(len(matrix)):
            matrix[row_index] = matrix[row_index][::-1]
        
        print(matrix)
        
        