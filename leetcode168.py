class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = []
        while n:
            if n % 26 == 0:
                ans.append('Z')
                n -= 26
            else:
                ans.append(chr(65+n % 26-1))
            n //= 26
        return ''.join(reversed(ans))
