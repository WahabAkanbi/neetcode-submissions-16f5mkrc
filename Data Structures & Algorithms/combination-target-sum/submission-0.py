class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #intuition: u can choose the value we are on
        # or choose another value
        # if its too big we move back
        output = []
        
        def dfs(total, index, subarray):
            if(total > target) or (index == len(nums)):
                return
            
            if(total == target):
                output.append(subarray.copy())
                return
    
            #if I dont choose, no need to copy
            dfs(total , index + 1, subarray)
            dfs(total + nums[index], index, subarray + [nums[index]])

        
        dfs(0, 0, [])
        return output
        #pass in an empty array repr subset
        #pass in current total also





        