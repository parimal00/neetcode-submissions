class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for o in operations:
            if o == "+":
                length = len(stack)
                data = stack[length-1] + stack[length-2]
                stack.append(data)
            
            elif o == "C":
                stack.pop()
            
            elif o == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(o))
        return sum(stack)
        