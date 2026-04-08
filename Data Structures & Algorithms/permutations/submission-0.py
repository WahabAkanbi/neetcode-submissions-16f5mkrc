class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []


        def dfs(subarray):
            if len(subarray) == len(nums):
                output.append(subarray)
                return

            for index in range(len(nums)):
                if(nums[index]  in subarray):
                    continue;
                else:
                    subarray.append(nums[index])
                    dfs(subarray.copy())
                    subarray.pop()
    

        #pick each index to start off with
        for index in range(len(nums)):
            dfs([nums[index]])
        
        return output
        