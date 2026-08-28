class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0 
        Stack = []
        
        for i, h in enumerate(heights):

            start = i

            while Stack and Stack[-1][1] > h:

                j, height = Stack.pop() 
                maxArea = max(maxArea, height * (i - j))
                start = j
            Stack.append((start,h))

        for i, height in Stack:
            maxArea = max(maxArea, height * (len(heights) - i))

        return maxArea



       
            