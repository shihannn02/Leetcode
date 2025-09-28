class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        max_len = 0
        subchar = {}  # {subchar} = index

        for right in range(len(s)):
            if s[right] in subchar and subchar[s[right]] >= left:
                left = subchar[s[right]]+1 # update the left idx, +1 not include the repeat one
            subchar[s[right]] = right # update new char
            max_len = max(max_len, right-left+1)

        return max_len