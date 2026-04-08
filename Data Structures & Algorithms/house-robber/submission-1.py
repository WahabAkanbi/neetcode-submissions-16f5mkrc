class Solution:
    def rob(self, nums: List[int]) -> int:
        #start at very end of the street
        house_robbed = {}
        num_house = len(nums)
        def rob_recurse(house_num): #max profit at house <housenum>
            if(house_num >= num_house):
                return 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            
            if(house_num not in house_robbed):            
            #skip it
                rob_sum = nums[house_num] + rob_recurse(house_num + 2)
                skip_sum = rob_recurse(house_num + 1)

                house_robbed[house_num] = max(rob_sum, skip_sum)


            return house_robbed[house_num]

        max_money = rob_recurse(0)
        return max_money
        #we can go back one or 2 all the way back
        