class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = nums[0]
        
        for index in range(1, len(nums)):
            output = output ^ nums[index]
        
        return output
        