m = {')':'(', '}':'{', ']':'['}
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        for c in s:
            if c in m.values():
                stack.append(c)
            elif c in m.keys():
                if not stack or stack.pop() != m[c]:
                    return False
            else:
                return False
        return not stack
                        
