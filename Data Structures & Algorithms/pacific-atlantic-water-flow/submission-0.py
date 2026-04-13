from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_len = len(heights)
        col_len = len(heights[0])
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        output = set()
        pacific = set()
        atlantic = set()

        def BFS(row_id, col_id, sea):
            queue = deque()
            queue.append((row_id, col_id))
            sea.add((row_id, col_id))

            while queue:
                row, col = queue.popleft()

                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy
                    if ((0<=new_row <row_len ) and (0<=new_col<col_len)):
                        if((new_row, new_col) not in sea):
                            if(heights[new_row][new_col] >= heights[row][col]):
                                #if the new row_is bigger then it means that we can get there
                                sea.add((new_row, new_col)) #if it works add it to seen list
                                queue.append((new_row, new_col))
            return sea
                #check to see if you can get to pacific and atlantic from here


        
        #call bfs on all top bottom

        #afyer each run our goal is to go uphill
        for col_id in range((len(heights[0]))):
            BFS(0, col_id, pacific)
            BFS(len(heights)-1, col_id, atlantic)

        for row_id in range(len(heights)):
            BFS(row_id, 0, pacific)
            BFS(row_id, len(heights[0]) -1, atlantic)

        return list(pacific & atlantic)

        

            

        