class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        total = 0
        answers = []
        for i in range(len(tokens)):
            if is_number(tokens[i]):
                answers.append(tokens[i])
            elif tokens[i] == "+":
                second = answers.pop()
                first = answers.pop()
                answers.append(int(first) + int(second))
            elif tokens[i] == "-":
                second = answers.pop()
                first = answers.pop()
                answers.append(int(first) - int(second))
            elif tokens[i] == "*":
                second = answers.pop()
                first = answers.pop()
                answers.append(int(first) * int(second))
            elif tokens[i] == "/":
                second = answers.pop()
                first = answers.pop()
                answers.append(int(int(first) / int(second)))
        return int(answers[-1])