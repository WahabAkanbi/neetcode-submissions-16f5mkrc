class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        nums 
        for index, val in enumerate(nums):
            complement = target - val
            if(complement in dic):
                return [dic[complement], index]
            else:
                dic[val] = index


        