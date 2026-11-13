class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use stack 
        # Iterate through array and add opearand to stack
        # If you find an operator, pop the operands in the stack,
        # perform the operation , and append the result in the stack

        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]