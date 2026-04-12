class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = nums[0]
        min_jump = 1
        furthest = 0
        #window will be left and right
        if(len(nums) == 1):
            return 0
        
        for index in range(len(nums)-1):
            if(index == right):#exceed our current window
                min_jump+= 1
                left = right + 1
                right = max(furthest, index + nums[index])
            furthest = max(furthest, index + nums[index])
        return min_jump