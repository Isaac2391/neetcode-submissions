class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        Stack = [] 

        for c in tokens:
            if c == "+":
                Stack.append(Stack.pop() + Stack.pop())
            elif c == "-":
                x,y = Stack.pop(), Stack.pop() 
                Stack.append(y-x)
            elif c == "/":
                x,y = Stack.pop(), Stack.pop()
                Stack.append(int(y/x))
            elif c == "*":
                Stack.append(Stack.pop() * Stack.pop()) 
            else:
                Stack.append(int(c))

        return Stack[0]


                
