import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min k where all nanas are eaten in k hours

        left = 1
        right = max(piles) #the max amount you can eat

        while left < right:
            # we try out a value of k and see if it works?
            k = int(((right - left) / 2) + left)
            total = 0
            for val in piles:
               total += math.ceil(val / k)
            if(total <= h):
                #try a smaller k
                right = k
            else:
                # k is too small, try a bigger k
                left = k + 1
        return right

        