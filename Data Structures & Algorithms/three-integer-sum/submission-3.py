class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []

        def twosum(complement, index):
            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if(total == complement):
                    output.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while(nums[left] == nums[left -1] and (left < right)):
                        left += 1
        
                    while(nums[right] == nums[right + 1] and (left < right)):
                        right -= 1
                
                elif(total < complement):
                    left += 1
                elif(total > complement):
                    right -= 1



        for index, value in enumerate(nums):
            if(index > 0):
                if (nums[index] == nums[index -1]):
                    continue
            complement = 0 - value
            twosum(complement, index)

        return output


