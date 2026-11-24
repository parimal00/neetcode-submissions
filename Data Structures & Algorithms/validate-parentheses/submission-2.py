class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack=[]
        for char in s:
            if char in data:
                if len(stack) > 0:
                    paran = stack.pop()
                    if paran != data[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) ==0:
            return True
        else:
            return False
            