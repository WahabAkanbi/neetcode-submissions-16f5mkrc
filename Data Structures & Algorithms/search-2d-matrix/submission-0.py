class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Not flattening
        row_len = len(matrix) #3 
        col_len = len(matrix[0]) # 4
        right = row_len*col_len
        left = 0


        while left < right:
            mid = ((right - left) // 2) + left
            #transform midpoint to an array
            row_id = mid // col_len
            col_id = mid % col_len
            if(matrix[row_id][col_id] == target):
                return True
            elif(matrix[row_id][col_id] < target):
                left = mid + 1
            elif(matrix[row_id][col_id] > target):
                right = mid
        return False
