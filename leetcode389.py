class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def toList(s):
            temp = []
            for i in range(len(s)):
                temp.append(s[i])
            return Counter(temp)
        if len(s) == 0:
            return t
        if len(list(toList(s))) < len(list(toList(t))):
            return [t[i] for i in range(len(t)) if t[i] not in s[0:]][0]
        else:
            return list(toList(t) - toList(s))[0]
