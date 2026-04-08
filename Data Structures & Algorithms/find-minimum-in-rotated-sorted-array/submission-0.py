class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        #keep track of left and right to find the original sorted

        while left < right:
            midpoint = ((right - left) // 2) + left

            #since midpoint = 2
            if(nums[midpoint] > nums[right]): #right half has what we need
                left = midpoint + 1
            else:
                #left half has midpoint
                right = midpoint
        return nums[left]

        