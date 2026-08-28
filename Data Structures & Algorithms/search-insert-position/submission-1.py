class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        res = len(nums)
        lo,hi = 0,len(nums) - 1

        while lo <= hi: 

            mid = (hi + lo) // 2

            if nums[mid] == target: 
                return mid
            elif nums[mid] > target:
                res = mid
                hi = mid - 1
            else: 
                lo = mid + 1
        return res
        
        