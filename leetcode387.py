class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        i = 0
        while i < len(s):
            if s[i] not in s[i+1:]:
                if s[i] not in s[0:i]:
                    return i
                    break
            i += 1
        return -1
