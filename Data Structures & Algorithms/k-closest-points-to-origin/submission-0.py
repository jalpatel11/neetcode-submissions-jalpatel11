class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq=[]

        for i in points:
            x,y=i
            dis=math.sqrt(x*x+y*y)
            heapq.heappush(pq,[dis,i])
        ans=[]
        while k:
            temp=heapq.heappop(pq)
            ans.append(temp[1])
            k-=1
        return ans