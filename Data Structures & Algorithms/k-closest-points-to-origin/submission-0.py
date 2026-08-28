import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = [] 
        DistanceToCoord = []
        heap = [] 

        for p in points:
            distance = self.euclideanDistance(p[0],p[1],0,0)
            DistanceToCoord.append((distance,p))

        for val in DistanceToCoord:
            heap.append(val)

        heapq.heapify(heap)

        while len(res) < k:
            kClosest= heapq.heappop(heap)[1]
            res.append(kClosest)
        
        return res
    
    def euclideanDistance(self,x1,y1,x2,y2):

        return math.sqrt(((x1-x2)**2) + ((y1-y2)**2))