import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if k == len(nums):
            return min(nums)
        elif k == 1:
            return max(nums)

        Kheap = nums[:]
        heapq.heapify(Kheap)

        while len(Kheap) > k:
            heapq.heappop(Kheap)

        return heapq.heappop(Kheap) 
