class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_vol = 0
        volume = 0

        while left < right:
            volume = (right - left) * min(heights[right] , heights[left])
            max_vol = max(max_vol, volume)
            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        
        return max_vol


        