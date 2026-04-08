class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0] * (n+1)
        result[0] = 1
        result[1] = 1
        for num in range(2, n+1):
            result[num] = result[num - 1] + result[num-2]

        return result[n]

        