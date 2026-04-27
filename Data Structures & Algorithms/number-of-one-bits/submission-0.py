class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n != 0:
            bit = n & 0x1
            if(bit):
                total += 1
            n = n >> 1
        
        return total

        