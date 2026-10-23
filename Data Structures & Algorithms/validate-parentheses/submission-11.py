class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for character in s:
            if character in pairs:
                if len(stack) == 0 or stack.pop() != pairs[character]:
                    return False
            else:
                stack.append(character)

        return len(stack) == 0