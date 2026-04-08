class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = set()
        def dfs(index, subset):
            if (index == len(nums)):
                insert_val = tuple(sorted(subset.copy()))
                output.add(insert_val)
                return


            #do not choose
            dfs(index + 1, subset)
            dfs(index + 1, subset+ [nums[index]])
        dfs(0, [])
        return [list(val) for val in output]






        