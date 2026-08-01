class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []
        backward = []
        for i in range(len(s)):
            if s[i].isalnum():
                forward.append(s[i].lower())
        for j in range(len(s) - 1, -1, -1):
            if s[j].isalnum():
                backward.append(s[j].lower())
        return forward == backward