class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]] #fast ptr


        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]
        
        # we need to find the cycle start
        return slow
        