class Solution:
    def rob(self, nums: List[int]) -> int:
        total_house = len(nums) 
        if(total_house == 1):
            return nums[0]

        houses_profit = {}
        def rob_house(start, end):
            # if we rob house 0 we cant rob house i -1

            if(start >= end):
                return 0

            #decision: rob house, skip
            if ((start,end) not in houses_profit):
                rob_path = nums[start] + rob_house(start + 2, end)
                skip_path = rob_house(start + 1, end)
                profit_house = max(rob_path, skip_path)   
                houses_profit[(start, end)] = profit_house

            return houses_profit[(start, end)]   

        
        #ignore last house
        #range
        return max(rob_house(0, total_house - 1), rob_house(1, total_house))