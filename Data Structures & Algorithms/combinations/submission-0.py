class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if k == n:
            return [[i for i in range(1,n+1)]] 

        result = [] 

        def backtrack(start, combination):

            if len(combination) == k:
                result.append(combination.copy())
                return 

            for i in range(start,n+1):

                combination.append(i)
                backtrack(i + 1,combination)
                combination.pop()

        backtrack(1,[])

        return result