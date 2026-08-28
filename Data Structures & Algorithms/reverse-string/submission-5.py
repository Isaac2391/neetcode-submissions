class Solution:

    import math 

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        p1,p2 = 0,len(s) - 1

        for i in range(len(s)):

           while p1 < p2:
            s[p1],s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1