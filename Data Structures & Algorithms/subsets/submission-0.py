class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(index, subset):
            #at each index, we have a choice to include the val or not
            if(index == len(nums)):
                output.append(subset)
                return 
            
            #do not include
            dfs(index+1, subset.copy())
            dfs(index+1 , subset + [nums[index]])

        dfs(0, [])
        return output
        