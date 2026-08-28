class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        Stack = []
        res = [] 

        def backtrack(openN, closedN):

            if openN == closedN == n:
                res.append("".join(Stack))
                return 
            
            if openN < n:
                Stack.append("(")
                backtrack(openN + 1, closedN)
                Stack.pop() 

            if closedN < openN:
                Stack.append(")")
                backtrack(openN, closedN + 1)
                Stack.pop()

        backtrack(0,0)

        return res

            

