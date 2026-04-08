import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        heap = []
        #count frequency
        for v in nums:
            if v in dic:
                dic[v] += 1
            else:
                dic[v] = 1

        for key, val in dic.items():
            heapq.heappush(heap,(val, key))
            if(len(heap) > k):
                heapq.heappop(heap)
        
        output = []
        for val, key in heap:
            output.append(key)
            
        return output