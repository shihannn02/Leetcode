class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLen = 0 # define the length
        read = 0
        while read < len(s):
            write = read+1
            if s[write] != s[read]:
                write += 1
            else:
                read = write