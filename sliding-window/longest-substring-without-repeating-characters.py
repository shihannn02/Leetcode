class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = r = 0
        n = len(s)
        maxLen = 0

        while r < n:
            if s[r] in d and d[s[r]] >= l:
                l = d[s[r]] + 1
            d[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen
