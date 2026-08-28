class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        Stack = [] 

        for index,temperature in enumerate(temperatures):
            
            while Stack and temperature > Stack[-1][0]:
                stackT,stackInd = Stack.pop() 
                res[stackInd] = (index - stackInd)
            Stack.append([temperature,index])

        return res
                


        