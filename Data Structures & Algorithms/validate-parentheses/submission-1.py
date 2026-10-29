class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) > 0 and match[c] == stack[-1]:
                stack.pop(-1)
            else:
                return False
        
        return len(stack) == 0
