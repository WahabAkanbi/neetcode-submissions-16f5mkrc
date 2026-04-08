import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = []
        for value in nums:
            heapq.heappush(heap,value)
            if(len(heap) > k):
                _ = heapq.heappop(heap)
        self.k = k
        self.heap = heap


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if(len(self.heap) > self.k):
            heapq.heappop(self.heap)
        return self.heap[0]

        
