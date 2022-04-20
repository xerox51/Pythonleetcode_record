class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum([(ord(columnTitle[i])-64)*pow(26, len(columnTitle)-1-i) for i in range(len(columnTitle))])
