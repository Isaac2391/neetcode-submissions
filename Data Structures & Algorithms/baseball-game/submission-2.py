class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = [] 
        symbols = ["C","D","+"]

        l = 0

        for op in operations:

            if op not in symbols:
                stack.append(int(op))

            elif op == "C":
                stack.pop(l)

            elif op == "D":
                c = stack[l] * 2 
                stack.append(int(c)) 
            
            elif op == "+":
                c = (stack[l] + stack[l-1])
                stack.append(int(c)) 
            

            l = len(stack) - 1

        return sum(stack)

            