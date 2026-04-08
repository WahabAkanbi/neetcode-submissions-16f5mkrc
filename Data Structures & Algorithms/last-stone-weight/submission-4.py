import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        if (len(stones) == 1):
            return stones[0]
        stones = [x * -1 for x in stones]

        #make it negative
        heapq.heapify(stones)



        while len(stones) > 1:
            biggest = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            diff = biggest - second
            heapq.heappush(stones, diff * -1)
        
        return -stones[0]


        