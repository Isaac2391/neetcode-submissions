import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            firstHeaviest = -heapq.heappop(stones)
            secondHeaviest = -heapq.heappop(stones)

            if firstHeaviest == secondHeaviest:
                pass
            else:
                heapq.heappush(stones,-(firstHeaviest - secondHeaviest))

        return -stones[0] if stones else 0