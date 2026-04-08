import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = -((x**2 + y**2))
            heapq.heappush(heap, (distance, [x,y]))
            if(len(heap) > k):
                heapq.heappop(heap)
        output = [distance for _ , distance in heap]
        return output

        