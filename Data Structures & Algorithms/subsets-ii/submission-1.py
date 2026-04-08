class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        def dfs(index, subset):
            if (index == len(nums)):
                insert_val = tuple(sorted(subset.copy()))
                output.add(insert_val)
                return
            next_index = index
            while next_index < len(nums) and nums[index] == nums[next_index]:
                next_index += 1

            #do not choose
            dfs(next_index, subset)
            dfs(index + 1, subset+ [nums[index]])
        dfs(0, [])
        return [list(val) for val in output]






        