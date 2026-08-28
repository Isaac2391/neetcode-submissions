class Solution:
    def validPalindrome(self, s: str) -> bool:

        start, end = 0, len(s) - 1 

        while start < end: 

            if s[start] != s[end]:

                removeStart, removeEnd = s[start + 1: end + 1], s[start:end]

                return (removeStart == removeStart[::-1] or removeEnd == removeEnd[::-1])

            start += 1
            end -= 1

        return True