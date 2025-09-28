class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']':'[', '}':'{'}

        for i in s:
            if i not in mapping.values():
                stack.append(i)
            else:
                if not stack or stack[-1]!=mapping[i]:
                    return False
                stack.pop()
        return not stack