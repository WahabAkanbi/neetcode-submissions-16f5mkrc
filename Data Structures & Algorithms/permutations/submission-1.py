class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []


        def dfs(subarray):
            if len(subarray) == len(nums):
                output.append(subarray)
                return

            for val in nums:
                if(val in subarray):
                    continue;
                else:
                    subarray.append(val)
                    dfs(subarray.copy())
                    subarray.pop()
    
        dfs([])
        
        return output
        