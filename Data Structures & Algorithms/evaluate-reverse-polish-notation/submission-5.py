class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "*", "-", "/"]
        
        for ent in tokens:
            if ent not in operators: 
                stack.append(int(ent))
            else:
                b = stack.pop()
                a = stack.pop()
                res = 0
                
                if ent == "+":
                    res = a + b
                elif ent == "*":
                    res = a * b
                elif ent == "-":
                    res = a - b
                elif ent == "/":
                    res = int(a / b)

                stack.append(res)
        return stack[0] 
