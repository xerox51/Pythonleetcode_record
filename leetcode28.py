class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if haystack.startswith(needle):
            return 0
        i = 0
        flag = False
        while i < len(haystack)-len(needle)+1:
            if haystack[i:i+len(needle)] == needle:
                return i
                flag = True
                break
            i += 1
        if flag:
            return i
        else:
            return -1
