class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = dict()
        s2 = dict()
        for c in s:
            if c not in s1:
                s1[c] = 0
            else:
                s1[c] += 1
        for c in t:
            if c not in s2:
                s2[c] = 0
            else:
                s2[c] += 1
        return s1 == s2