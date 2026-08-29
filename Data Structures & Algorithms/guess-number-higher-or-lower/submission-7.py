# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


# Notes

# Binary search ( we know the range, 1 -> n, so we can reduce the search space each iteration)
# Two pointers ( part of binary search )
# Recursion ( recursively call method on the smaller search space until answer is found)

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # 0 equal 
        # -1 means guess is higher than pick
        # 1 means guess lower than pick

            if n == 1:
                return 1 

            l,r = 1,n 

            while True:

                mid = (l + r) // 2 

                result = guess(mid) 

                if result > 0:
                    l = mid + 1

                elif result < 0:

                    r = mid - 1

                else:

                    return mid
