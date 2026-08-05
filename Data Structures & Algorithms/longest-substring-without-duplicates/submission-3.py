class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        left = 0
        right = 0
        longest = 0
        while right <= len(s) - 1:
            cur_longest = 0
            if s[right] not in uniques:
                uniques.add(s[right])
                right += 1
            else:
                while s[right] in uniques:
                    uniques.remove(s[left])
                    left += 1
                uniques.add(s[right])
                right += 1
            cur_longest = len(s[left:right])
            if cur_longest > longest:
                longest = cur_longest
        return longest