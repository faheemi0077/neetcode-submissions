class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = dict()
        counts_t = dict()
        for i in range(len(s)):
            if s[i] not in counts_s.keys():
                counts_s[s[i]] = 1
            else:
                counts_s[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in counts_t.keys():
                counts_t[t[i]] = 1
            else:
                counts_t[t[i]] += 1
        return counts_s == counts_t