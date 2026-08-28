class Solution:
    def isValid(self, s: str) -> bool:

        Stack = [] 

        bracketPairs = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in bracketPairs:
                if Stack and Stack[-1] == bracketPairs[char]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(char)

        return True if not Stack else False

                      





            
