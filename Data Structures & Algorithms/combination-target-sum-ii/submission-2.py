class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = set()
        def dfs(index, total,  subset):
            #first case our total is the same as target
            if total == target:
                inserted_val = tuple(sorted(subset.copy()))
                output.add(inserted_val)
                return

            if (index == len(candidates) or (total > target)):
                return

            next_index = index
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            #choose it branch, index has to still move
            dfs(index+1, total + candidates[index], subset + [candidates[index]])
            # do not choose
            dfs(next_index, total , subset)

        
        dfs(0, 0 , []) #total, current index, current subset
        return [list(val) for val in output]