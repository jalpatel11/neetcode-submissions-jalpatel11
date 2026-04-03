class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [i * -1 for i in stones]
        heapq.heapify(heap)
        
        while heap:
            if len(heap)==1:
                break
            y=-1*heapq.heappop(heap)
            x=-1*heapq.heappop(heap)

            if x!=y:
                heapq.heappush(heap,-(y-x))
            
        
        if heap:
            return -1*heapq.heappop(heap)
        return 0