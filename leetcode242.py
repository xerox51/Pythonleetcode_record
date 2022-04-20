class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def toList(s):
            temp = []
            for i in range(len(s)):
                temp.append(s[i])
            return temp

        return Counter(toList(s)) == Counter(toList(t))
