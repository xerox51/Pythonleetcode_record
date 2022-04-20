class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def getsum(s):
            temp = []
            i = 0
            count = []
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    count.append(True)
                    i += 1
                    if i == len(s) - 1:
                        break
                if s[i] != s[i+1]:
                    count.append(False)
                    i += 1
                    if i == len(s) - 1:
                        break
            return count

        def getindex(s):
            index = []
            count_s = []
            for i in range(len(s)):
                count_s.append(s[i])
            count_s.reverse()
            for item in set(count_s):
                index.append(count_s.index(item))
            return sorted(index)

        if len(s) == 1:
            return True
        else:
            if getsum(s) == getsum(t):
                if getindex(s) == getindex(t):
                    return True
            return False
