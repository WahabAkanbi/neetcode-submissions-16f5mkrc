class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we always start at 0, 0 and end at m-1, n-1
        memo = {}

        def recurse(row, col):
            if(row > m-1) or (col > n-1):
                return 0
            
            if(row == m-1) and (col == n-1):
                return 1
    
            #go down once
            if((row, col) not in memo):
                output = recurse(row+1, col)
                output += recurse(row, col + 1)
                memo[(row, col)] = output

            return memo[(row, col)]


        return recurse(0, 0)
        