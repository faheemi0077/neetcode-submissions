class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        frequencies = dict()
        longest = 0
        while right <= len(s) - 1:
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1
            right += 1
            while len(s[left:right]) - max(frequencies.values()) > k:
                frequencies[s[left]] -= 1
                left += 1
            if len(s[left:right]) >= longest:
                longest = len(s[left:right])
        return longest