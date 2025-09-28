class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abaca -> s[a]=0 left=0,s[b]=1, s[a]=2 left=1
        shash = {}
        left, sLen = 0
        for right, char in enumerate(s):
            if char in shash:
                left = shash[char]+1
            shash[char] = right
            sLen = max(sLen, right - left + 1)
        return sLen
            


            