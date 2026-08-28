class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        r = k
        l = 0

        while r <= len(nums):
            
            currentWindow = nums[l:r]
            res.append(max(currentWindow))
            l += 1
            r += 1

        return res 
