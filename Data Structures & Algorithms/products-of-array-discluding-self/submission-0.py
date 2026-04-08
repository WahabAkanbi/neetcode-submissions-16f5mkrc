class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        total_left = 1
        for i in range(len(nums)):
            result[i] = total_left
            total_left *= nums[i]

        total_right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= total_right
            total_right *=nums[i]
        
        return result


        