class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        return stack == []