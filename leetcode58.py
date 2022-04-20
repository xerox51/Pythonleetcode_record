class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()
        if len(temp) == 1:
            return len(temp[0])
        else:
            return len(temp[len(temp)-1])
