class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # 1. Iterate through array 
        # 2.  Add value to the array 
        # 3. Recursively add value + next to array 
        # 4. Return when array is done 

        # Edge cases: empty array

        res = []
        n = len(nums)

        res,sol = [],[]

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return 

            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res

        
