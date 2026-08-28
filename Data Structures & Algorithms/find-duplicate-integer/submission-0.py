class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        nums = sorted(nums)

        firstPointer,secondPointer = 0,1 

        while secondPointer <= len(nums):

            if nums[firstPointer] == nums[secondPointer]:

                return nums[firstPointer]

            firstPointer += 1
            secondPointer += 1
            
                   