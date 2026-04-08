class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = set()

        def dfs(index, total, subset):
            if(total == target):
                to_sort = sorted(subset.copy())
                output.add(tuple(to_sort))
                return

            if(index == len(candidates)) or (total> target):
                return


            dfs(index+ 1, total, subset)#do not take branch
            dfs(index+1,total + candidates[index], subset+[candidates[index]]) #take branch
            


        dfs(0, 0, [])# curr total, index, currSubset
        return [list(val) for val in output]     
        