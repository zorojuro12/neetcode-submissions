class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for br in s:
            if br in brackets:
                if not stack or stack[-1] != brackets[br]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(br)
        return True if not stack else False