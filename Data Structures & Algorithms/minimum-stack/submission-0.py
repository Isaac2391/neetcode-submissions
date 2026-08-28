class MinStack:

    def __init__(self):

        self.Stack = []

    def push(self, val: int) -> None:

        self.Stack.append(val)
        
    def pop(self) -> None:

        self.Stack.pop()
        

    def top(self) -> int:
        
        return self.Stack[-1]       

    def getMin(self) -> int:

        minVal = float("infinity")

        for i in range(len(self.Stack)):
            if self.Stack[i] < minVal:
                minVal = self.Stack[i]

        return minVal 
        
