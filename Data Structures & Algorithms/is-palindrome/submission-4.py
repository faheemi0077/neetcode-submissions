class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left].lower().isalnum() and s[right].lower().isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            elif s[left].lower().isalnum() and not s[right].lower().isalnum():
                right -= 1
            elif not s[left].lower().isalnum() and s[right].lower().isalnum():
                left += 1
            else:
                left += 1
                right -= 1
        return True