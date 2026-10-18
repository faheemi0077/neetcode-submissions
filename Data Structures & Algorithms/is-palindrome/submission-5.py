class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                j = s[left].lower()
                k = s[right].lower()
                if j != k:
                    return False
                else:
                    left += 1
                    right -= 1
            elif s[left].isalnum() == False and s[right].isalnum() == True:
                left += 1
            elif s[left].isalnum() == True and s[right].isalnum() == False:
                right -= 1
            else:
                left += 1
                right -= 1
        return True