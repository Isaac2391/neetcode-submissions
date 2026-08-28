class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 0:
            return -1

        lo,hi = 0,len(nums) - 1

        while lo <= hi:

            mid = (lo + hi) // 2

            if nums[mid] > target:
                hi -= 1
            elif nums[mid] < target:
                lo += 1
            elif nums[mid] == target:
                return mid

        return -1 

        