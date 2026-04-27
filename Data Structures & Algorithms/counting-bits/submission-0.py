class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        
        def numones(n):
            total = 0

            while n != 0:
                bit = n & 0x1
                if(bit):
                    total += 1
                n = n >> 1
        
            return total

        for i in range(n+1):
            output[i] = numones(i)
        
        return output
            

        