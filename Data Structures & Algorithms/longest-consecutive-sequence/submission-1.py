class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)

        longest = 0
        for value in nums:
            length = 1
            temp = value

            while temp + 1 in checker:
                temp = temp + 1
                length += 1
            
            longest = max(longest, length)
        return longest       