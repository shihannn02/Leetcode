class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l,r = 0,0
        n = len(s)
        maxLen = 0
        while r<n:
            if s[r] in d:
                l = max(l, d[s[r]]+1)
                length = r-l+1
                maxLen = max(length, maxLen)
                d[s[r]] = r
                r+=1
        return maxLen
            


            