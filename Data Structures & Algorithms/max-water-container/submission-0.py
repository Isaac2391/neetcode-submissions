class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0 
        lo,hi = 0,len(heights) - 1

        while lo < hi:
            area = ( hi - lo) * min(heights[lo], heights[hi])
            res = max(res,area)

            if heights[lo] < heights[hi]:
                lo += 1
            else: 
                hi -= 1

        return res