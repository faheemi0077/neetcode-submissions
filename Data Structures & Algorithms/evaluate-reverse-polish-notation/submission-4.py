class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            buffer = []
            if tokens[i] in [str(j) for j in range(-200, 201)]:
                stack.append(tokens[i])
            elif tokens[i] == "+":
                buffer.append(stack.pop())
                buffer.append(stack.pop())
                res = int(buffer[0]) + int(buffer[1])
                stack.append(res)
            elif tokens[i] == "-":
                buffer.append(stack.pop())
                buffer.append(stack.pop())
                res = int(buffer[1]) - int(buffer[0])
                stack.append(res)
            elif tokens[i] == "*":
                buffer.append(stack.pop())
                buffer.append(stack.pop())
                res = int(buffer[0]) * int(buffer[1])
                stack.append(res)
            elif tokens[i] == "/":
                buffer.append(stack.pop())
                buffer.append(stack.pop())
                res = int(buffer[1]) / int(buffer[0])
                stack.append(res)
        return int(stack[0])