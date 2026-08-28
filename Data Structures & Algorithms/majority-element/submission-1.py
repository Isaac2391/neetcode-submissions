class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        number_occurences = {}

        if len(nums) == 1:
            return nums[0]

        for number in nums:

            if number in number_occurences: 
                number_occurences[number] += 1 
                if number_occurences[number] >= (len(nums)/2):
                    return number
            
            else:

                number_occurences[number] = 1